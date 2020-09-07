from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """Registration of new user"""
    if request.method != 'POST':
        # Displaying empty user registration form
        form = UserCreationForm()
    else:
        # Processing filled form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Logging new user and redirecting him to main page
            login(request, new_user)
            messages.success(request, f'Registered user "'
                                      f'{new_user.username}"')
            return redirect('learning_logs:index')
    # Displaying empty form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
