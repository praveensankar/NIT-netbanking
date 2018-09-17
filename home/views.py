
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

from .models import User,Account


def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def dashboard(request,username):
    user=User.objects.get(username=username)
    user_account = Account.objects.get(username=user)
    template = loader.get_template('home/dashboard.html')
    context = {
        'account':user_account,
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('home/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('home/register.html')
    context = {}
    return HttpResponse(template.render(context, request))


def postregister(request):
    try:
        u_name = request.POST['username']
        user = User(username=request.POST['username'], password=request.POST['password'])

    except ():
        # Redisplay the question voting form.
        return render(request, 'home/login.html', {

            'error_message': "You didn't select a choice.",
        })
    else:

        user.save()
        a=Account(username=user,balance=2500)
        a.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('home:dashboard', args=(u_name,)))


# ...
def postlogin(request):
    try:
        u_name=request.POST['username']
        user=User.objects.get(username=u_name)

    except ():
        # Redisplay the question voting form.
        return render(request, 'home/login.html', {

            'error_message': "You didn't select a choice.",
        })
    else:


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('home:dashboard', args=(u_name,)))




def transfer(request,username):
    user=User.objects.get(username=username)
    user_account = Account.objects.get(username=user)

    template = loader.get_template('home/transfer.html')
    context = {
        'account':user_account,
    }
    return HttpResponse(template.render(context, request))


# ...
def posttransfer(request):
    try:
        u_name=request.POST['username']
        amount=int(request.POST['amount'])
        current_username=request.POST['current_user']
        fromUser=User.objects.get(username=current_username)
        toUser=User.objects.get(username=u_name)
        fromAccount=Account.objects.get(username=fromUser)
        toAccount=Account.objects.get(username=toUser)
        fromAccount.balance=fromAccount.balance-amount
        toAccount.balance=toAccount.balance+amount

    except ():
        # Redisplay the question voting form.
        return render(request, 'home/login.html', {

            'error_message': "You didn't select a choice.",
        })
    else:


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        fromAccount.save()
        toAccount.save()
        return HttpResponseRedirect(reverse('home:dashboard', args=(current_username,)))