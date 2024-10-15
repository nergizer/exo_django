from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import QuestionForm
from .models import Question, Choice


# Create your views here.


def statisitcs(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"sondages": Question.objects.count(),"choix" : Choice.objects.count()}
    return render(request, "polls/statistics.html", context)

def question(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise PermissionDenied()
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            qs = Question(None,form.cleaned_data.get("question"),timezone.now())

            qs.save()

            i = 0

            while "reponse" + str(i) in form.cleaned_data:
                rep = form.cleaned_data.get("reponse"+str(i))
                if rep.strip() == "":
                    break
                Choice(None,qs.id,rep,0).save()
                i+= 1


            return HttpResponseRedirect("/polls/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, "polls/question.html", {"form": form})

class FreqView(generic.DetailView):
    template_name = "polls/frequency.html"
    model = Question

class LoginV(LoginView):
    template_name = "polls/login.html"
    next_page = "/polls/"


class AllView(generic.ListView):
    template_name = "polls/all.html"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("polls:index"))


def vote(request, question_id):
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
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)