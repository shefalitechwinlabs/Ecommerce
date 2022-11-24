from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset/password_reset_complete.html'), name='password_reset_complete'),
    path('email_verification/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/email_verification/email_verification_done.html'), name='email_verification_done'),
    path('emal_verification_complete/<uidb64>/<token>/', views.email_verification_complete, name='email_verification_complete'),
]
