from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "teams/index.html"
    context_object_name = "recently_uploaded"
    
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:7]


class DetailView(generic.DetailView):
    template_name = 'teams/detail.html'
    model = Question


class ResultsView(generic.DetailView):
    template_name = 'teams/results.html'
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question' : question,
            'error_message' : ' "You didn\'t select a choice.',
        }
        return render(request, 'vote.html', context)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question_id,) ))