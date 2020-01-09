from django.shortcuts import render, redirect

from django.contrib import messages
from .forms  import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # if post request assign userform with that post data
        if form.is_valid():
            form.save() #save the user
            username = form.cleaned_data.get('username') #if form is valid return the registered username
            messages.success(request, f'Account successfully created for {username}!') #Flash message to display to user
            return redirect('blog-home') # redirect to homepage after registeration
    else:
        form = UserRegisterForm() # if not post request assign   blank form
    return render(request, 'users/register.html', {'form': form})