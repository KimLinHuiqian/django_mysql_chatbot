from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

# Cr  (function) def chatbot(request:Any)-> HttpResponse
#receives the msg
def chatbot(request):
    if request.method =='POST':
        message=request.POST.get('message')
        if 'pig'in message:
            response='oink'
        else:
            response=_random_string()
        return JsonResponse({'message':message,'response':response})
    #render pages 
    return render(request,'chatbot.html')

    
# def chatbot(request):
#     chats = Chat.objects.filter(user=request.user)

#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = ask_openai(message)

#         chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
#         chat.save()
#         return JsonResponse({'message': message, 'response': response})
#     return render(request, 'chatbot.html', {'chats': chats})


def _random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    return random.choice(random_list)

@api_view(['GET'])
def _citizen_api(request):
    api_urls={
        'List':'/citizen-list/',
        'Detail View':'/citizen-detail/<int:citizen_id>',
        'Create':'/citizen-create/<int:citizen_id>',
        'Delete':'/citizen-delete/<int:citizen_id>',
        'Update':'/citizen-update/<int:citizen_id>'
    }
    
    return Response(api_urls)

@api_view(['GET'])
def _application_api(request):
    api_urls={
        'List':'/application-list/',
        'Detail View':'/application-detail/<int:application_id>',
        'Create':'/application-create/<int:application_id>',
        'Delete':'/application-delete/<int:application_id>',
        'Update':'/application-update/<int:application_id>'
    }
    
    return Response(api_urls)
