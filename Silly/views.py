from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer , ChatterBotCorpusTrainer

bot = ChatBot('Silly ChatBot', read_only = False,
                logic_adapters = [
                    {
                         
                            'import_path':'chatterbot.logic.BestMatch',
                            'default_response':'Sorry, I dont know what that means',
                            'maximum_similarity_threshold': 0.90
                    },
                    {
                            'import_path':'chatterbot.logic.TimeLogicAdapter',
                             'maximum_similarity_threshold': 0.90
                    }
                    ])
discussion = ChatterBotCorpusTrainer(bot)

test_chat_train = {
    "Hi",
    "Hi there",
    "What is your name?",
    "I'm Silly, Silly ChatBot",
    "What is your fav food?",
    "I like cheese",
    "Goodbye",
    "Thanks great to see you next"
}

list_trainer = ListTrainer(bot)
list_trainer.train(test_chat_train)

discussion.train('chatterbot.corpus.english','chatterbot.corpus.french')


def index(request):
    return render(request,'Silly/index.html')


def get_bot_response(request):
    userText = request.GET.get('msg')
    return HttpResponse(str(bot.get_response(userText)))


