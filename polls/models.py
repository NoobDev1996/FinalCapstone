"""

This .py file contains Django models for a simple question and choice system.

The Question model represents a question with a question text and the date it was published.
Its is defined as a subclass of the models.Model class
The __str__ method is overridden to return a string representation of the question
text.

The Choice model represents a choice with a choice text, This is also defined as a subclass of models.Model.
The question field is a foreign key to the Questions model establishing a one-to-many relationship
between questions and choices.The __str__ method is overridden to return a string representation of the choice
text.

These models define the structure and behavior of the data stored in the applications database.
They allow the application to create, retrieve, update, and delete question and choice objects in the database.

"""
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text