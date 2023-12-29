# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import StudentRegistrationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy


def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Registration successful")
    else:
        form = StudentRegistrationForm()

    return render(request, 'Account/student/register.html', {'form': form})

