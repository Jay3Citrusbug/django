from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def sign_up(request):
     msg = None
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('signin')
        else:
            msg = 'form is not valid'
     else:
        form = SignUpForm()
     return render(request,'signup.html', {'form': form, 'msg': msg})

    




def sign_in(request):

     form = LoginForm(request.POST or None)
     msg = None
     if request.method == 'POST':
        if form.is_valid():
             
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
          #   print(user)
            if user is not None:
               login(request, user)
               return redirect('home')
            else:
                msg= 'invalid credentials'
     else:
            msg = 'error validating form'
     return render(request, 'sign_in.html', {'form': form, 'msg': msg})
  
 
def home(request):
     return HttpResponse("<h1>welcome</h1>")





