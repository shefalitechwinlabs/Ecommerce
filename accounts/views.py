from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from .forms import *
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.http import HttpResponse
from .models import *
from products.models import Collections
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


def profile(request):
    if 'username' in request.session:
        context = {}
        user = request.user
        form = AddressForm()
        profile_obj = Profile.objects.get(created_by=user)
        address_obj = Address.objects.filter(created_by=user)
        product = Collections.objects.filter(added_by=user)
        # click event address form
        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.created_by = request.user
                address.save()
                messages.success(request, 'Address updated')    
                return redirect('/profile')
            else:
                form = AddressForm()
                context = {'dataset': profile_obj, 'form': form, 'collections': product}
                return render(request, 'accounts/profile/profile.html', context)
        context = {'profile': profile_obj, 'address': address_obj, 'form': form, 'collections':product}
        return render(request, 'accounts/profile/profile.html', context)
    else:
        return redirect('/accounts/login')

def edit_profile(request):
    if 'username' in request.session: 
        query_profile=Profile.objects.get(created_by=request.user)
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES, instance=query_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated')
                return redirect('/profile')
            else:
                messages.error(request, 'Profile not valid', )
                return render(request, 'accounts/profile/edit_profile.html', context)
        else:
            form = ProfileForm(instance=query_profile)
            context = {
                'profile': query_profile,
                'form': form,
            }
            return render(request, 'accounts/profile/edit_profile.html', context)
    return redirect('/')

def edit_address(request, id):
    if 'username' in request.session: 
        query_address=Address.objects.get(id=id)
        address_form_to_edit =AddressForm(request.POST or None, instance=query_address)
        
        if request.method == 'POST':
            if address_form_to_edit.is_valid():
                address_form_to_edit.save()
            messages.success(request, 'Address updated')
            return redirect('/profile')
        else:
            form = address_form_to_edit
            context = {
                'address': query_address,
                'form': form,
            }
            return render(request, 'accounts/profile/edit_address.html', context)
    return redirect('/')

def address_details(request):
    if 'username' in request.session:
        query_address=address_obj = Address.objects.filter(created_by=request.user)
        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.created_by = request.user
                address.save()
                messages.success(request, 'Profile updated')    
                return redirect('/profile')
            else:
                form = AddressForm()
                context = {'address': query_address, 'form': form}
                return render(request, 'accounts/profile/address_details.html', context)
        else:
            form = AddressForm()
            context = {
                'address': query_address,
                'form': form,
            }
            return render(request, 'accounts/profile/address_details.html', context)
    else:
        return redirect('/')

def activateEmail(request, user, to_email):
    messages.success(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')

def signup(request):
    form = SignupForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        #print(dict(request.POST.items()))
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # mail system
            htmly = get_template('accounts/email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'shefali.techwinlabs@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Profile created. You can log in now!')    
            return redirect('/accounts/login')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if 'username' in request.session:
        return redirect('home/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            messages.success(request, 'loggedin successfully')
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    username = request.session.get('username')
    del username
    return render(request, 'accounts/logout.html')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            print(data)
            associated_users = ExtendUser.objects.filter(Q(email=data))
            
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password/password_reset.html", context={"password_reset_form": password_reset_form})
