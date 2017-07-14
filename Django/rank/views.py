from django.shortcuts import render
from yahoo_finance import Share
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import IndexSignUpForm
import random

@login_required
def rank_list(request):
    tickers = {}
    fopen = open('../tickers.txt', 'r')
    for line in fopen:
        key = line.strip()
        price = get_price(key)
        tickers[key] = price
    fopen.close()

    return render(request, 'rank_list.html', {'tickers': tickers})

def get_price(name):
    company = Share(name)
    return company.get_price()
    #return random.randint(0,len(name))*42

def index(request):
     if request.method == "POST":
          form = IndexSignUpForm(request.POST)
          if form.is_valid():
               username = email = form.cleaned_data['email']
               first_name = form.cleaned_data['first_name']
               last_name = form.cleaned_data['last_name']
               password1 = form.cleaned_data['password1']
               password2 = form.cleaned_data['password2']
               #Need to do a check if password1 == password2 then do below
               
               user = User.objects.create_user(username, email, password1)
               user.first_name = first_name
               user.last_name = last_name
               user.save()
               
               new_user = authenticate(username=email, password=password1, )
               login(request, new_user)
               return HttpResponseRedirect('rank_list')
     else:
          form = IndexSignUpForm()
          
     return render(request, 'index.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

'''
def login(request):
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
        else:
            form = SignUpForm()
        return render(request, '', {'form': form})
'''

