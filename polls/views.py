"""

This .py file contains Django view functions for a polling application.
The views handle various aspects of the application, includeing rendering the poll page,
displaying the details of a specific poll, showing the results of a poll and
handling the users vote for a poll.

The views are decorated with @login_required which means the user needs to be authenticated
in order to use the polling application. If the user is not authenticated, they will be sent back
to the login page.

The detail view takes a question ID as a parameter and retrieves the corresponding question from the database.
If the question does not exist, a 404 error will be raised. The view then renders the html template
passing the question as context.

The `results` view is similar to the `detail` view. It retrieves the question based on the provided question ID,
raises a 404 error if the question does not exist, and renders the 'polls/results.html' template with the question
as context.

The `vote` view handles the user's vote for a specific question. It retrieves the question from the database using
the question ID. If the user has not selected a choice, or the choice does not exist, the view re-renders the 'polls/details.html'
template with an error message. If the choice is valid, the vote count for the choice is incremented, and the updated
choice is saved. Finally, the user is redirected to the 'polls:results' URL, which will display the results of the poll.

"""
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Choice, Question
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/user_auth/login/')
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

@login_required(login_url='http://127.0.0.1:8000/user_auth/login/')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

@login_required(login_url='http://127.0.0.1:8000/user_auth/login/')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required(login_url='http://127.0.0.1:8000/user_auth/login/')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/details.html', {'question': question, 'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))