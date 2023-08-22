from django.contrib.auth.models import User
from django.db import models
from datetime import date

CATEGORIES = (
    ('1', 'JS'), 
    ('2', 'Python'), 
    ('3', 'C#'), 
    ('4', 'C++'), 
    ('5', 'C'), 
    ('6', 'Ruby'),
)

TAGS = (
    ('1', 'Easy'), 
    ('2', 'Medium'), 
    ('3', 'Hard'),
)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=255)

class Answer(models.Model):
    content = models.TextField(max_length=255)
    creationtime = models.DateField('Created At ', null=True)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    category = models.CharField(
        max_length = 1,
        choices = CATEGORIES,
        default = CATEGORIES[0][0]
    )
    creationtime = models.DateField('Created At ', null=True)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Tag(models.Model):
    tags = models.CharField(
        max_length = 5,
        choices = TAGS,
        default = TAGS[0][0],
    )
    questions = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
