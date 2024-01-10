from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

# Create your views here.

# def index(request) -> HttpResponse:
#     """ This is the index of the polls app """
#     latest_questions = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_questions,
#     }
#     return HttpResponse(template.render(context, request))
#     # return render(request, "polls/index.html", context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]


def counter(request) -> HttpResponse:
    """ This is the counter of the polls app """
    return HttpResponse("Welcome to the polls counter page")


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """ excludes questions not yet published """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# def detail(request, question_id):
#     """ This gives the details for a question """
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     """ This returns the results of a question """
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    """ This shows the current question being voted on """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )