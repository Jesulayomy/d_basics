from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question

# Create your views here.

def index(request) -> HttpResponse:
    """ This is the index of the polls app """
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_questions,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, "polls/index.html", context)

def counter(request) -> HttpResponse:
    """ This is the counter of the polls app """
    return HttpResponse("Welcome to the polls counter page")

def detail(request, question_id):
    """ This gives the details for a question """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    """ This returns the results of a question """
    response = f"These are the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    """ This shows the current question being voted on """
    return HttpResponse(f"Voting on question {question_id}")
