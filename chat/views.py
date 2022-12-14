from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Avatar
from .models import *
from main.views import getAvatar

@login_required
def messages(request):
    return render(request, 'chat/messages.html', {'userAvatar': getAvatar(request.user), 'contacts': getContacts(request)})

@login_required
def newChat(request):
    if request.method == 'POST':
        try:
            contact = User.objects.get(username=request.POST['contact'])
            contact.avatar = getAvatar(contact)
            return render(request, 'chat/chat.html', {'userAvatar': getAvatar(request.user), 'contact': contact, 'messages': getContactMessages(request, contact), 'contacts': getContacts(request)})
        except:
            return render(request, 'chat/messages.html', {'userAvatar': getAvatar(request.user), 'contacts': getContacts(request), 'error': 'User not found'})

@login_required
def chat(request, username):
    try:
        contact = User.objects.get(username=username)
        contact.avatar = getAvatar(contact)
        return render(request, 'chat/chat.html', {'userAvatar': getAvatar(request.user), 'contact': contact, 'messages': getContactMessages(request, contact), 'contacts': getContacts(request)})
    except:
        return render(request, 'chat/chat.html', {'userAvatar': getAvatar(request.user), 'contacts': getContacts(request), 'error': 'User not found'})

@login_required
def sendMessage(request):
    if request.method == 'POST':
        message = Message.objects.create(sender=request.user, receiver=User.objects.get(username=request.POST['username']), message=request.POST['message'])
        message.save()
        return redirect('chat:chat', username=request.POST['username'])

################### Functions
def getContacts (request):
    if request.user.id:
        contacts = []
        for message in Message.objects.all().filter(sender=request.user):
            if message.receiver not in contacts:
                contacts.append(message.receiver)
        for message in Message.objects.all().filter(receiver=request.user):
            if message.sender not in contacts:
                contacts.append(message.sender)
        for contact in contacts:
            contact.avatar = getAvatar(contact)
        return contacts

def getContactMessages (request, contact):
    if request.user.id:
        messages = Message.objects.all().filter(sender=request.user, receiver=contact) | Message.objects.all().filter(sender=contact, receiver=request.user)
        for message in messages:
            message.sender.avatar = getAvatar(message.sender)
            if message.sender == request.user:
                message.sender.username = 'You'
        messages = reversed(messages)
        return messages
