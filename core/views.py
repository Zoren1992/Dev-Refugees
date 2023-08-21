from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from . models import User, Answer, Question, Tag


def home(request):
  return render(request, 'core/index.html')

def contact(request):
  return render(request, 'core/contact.html')