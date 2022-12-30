from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer

# chatbot
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """
    chatterbot = ChatBot(settings.CHATTERBOT)
    chatterbot = ChatBot('mania')

    # Training with Personal Ques & Ans 
    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome."
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    # Training with English Corpus Data 
    trainer_corpus = ChatterBotCorpusTrainer(chatbot)
    trainer_corpus.train(
        'chatterbot.corpus.english'
    ) 

    # # Create a new trainer for the chatbot
    # trainer = ChatterBotCorpusTrainer(chatbot)

    # # Train the chatbot based on the english corpus
    # trainer.train("chatterbot.corpus.english")

    # # Train based on english greetings corpus
    # trainer.train("chatterbot.corpus.english.greetings")

    # # Train based on the english conversations corpus
    # trainer.train("chatterbot.corpus.english.conversations")

    #  # Get a response to an input statement
    # chatbot.get_response("Hello, how are you today?")

    # def post(self, request, *args, **kwargs):
    #     """Return a response to the statement in the posted data.
    #     * The JSON data should contain a 'text' attribute."""

    #     input_data = json.loads(request.body.decode('utf-8'))

    #     if 'text' not in input_data:
    #         return JsonResponse({
    #             'text': [
    #                 'The attribute "text" is required.'
    #             ]
    #         }, status=400)

    #     response = self.chatterbot.get_response(input_data)
    #     response_data = response.serialize()

    #     return JsonResponse(response_data, status=200)

    # def get(self, request, *args, **kwargs):
    #     """Return data corresponding to the current conversation."""

    #     return JsonResponse({
    #         'name': self.chatterbot.name
    #     })