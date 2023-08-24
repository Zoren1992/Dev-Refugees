from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from . models import User, Answer, Question, Tag
from . forms import AnswerForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def home(request):
  return render(request, 'core/index.html')

def contact(request):
  return render(request, 'core/contact.html')

def signup(request):
  error_message = ''
  form = UserCreationForm(request.POST)
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def profile(request):
  return render(request, 'devs/profile.html')

def questions_index(request):
  questions = Question.objects.all()
  return render(request, 'questions/index.html', {
    'questions': questions
  })

def questions_detail(request, question_id):
  question = Question.objects.get(id=question_id)
  id_list = question.answers.all().values_list('id')
  answer_form = AnswerForm()
  return render(request, 'questiosns/detail.html', {
    'question': question, 'answer_form': answer_form,
  })

class questions_create(CreateView):
  model = Question
  fields = ['title', 'content', 'category', 'creationtime']

class questions_update(UpdateView):
  model = Question
  fields = ['content', 'category', 'creationtime']

class questions_delete(DeleteView):
  model = Question
  success_url = '/questions'

def add_answer(request, answer_id):
  form = AnswerForm(request.POST)
  if form.is_valid():
    new_answer = form.save(commit=False)
    new_answer.question_id = question_id
    new_answer.save()
  return redirect('detail', question_id=question_id)