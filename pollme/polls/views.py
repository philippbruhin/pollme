import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Choice, Poll
from .forms import PollForm

@login_required
def polls_list(request):
    """
    Renders the polls_list.html template which lists all the 
    currently available polls.
    """
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)

@login_required
def add_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            new_poll = form.save(commit=False)
            new_poll.pub_date = datetime.datetime.now()
            new_poll.owner = request.user
            new_poll.save()
            new_choice1 = Choice(
                poll = new_poll,
                choice_text=form.cleaned_data['choice1']
            ).save()
            new_choice2 = Choice(
                poll = new_poll,
                choice_text=form.cleaned_data['choice2']
            ).save()
            messages.success(request, 'Poll and choices added!', extra_tags='alert alert-success')
            return redirect('polls:list')
    else:
        form = PollForm()
    context = {'form': form}
    return render(request, 'polls/add_poll.html', context)

@login_required
def edit_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user != poll.owner:
        return redirect('/')
    return render(request, 'polls/edit_poll.html', {'poll': poll})


@login_required
def poll_detail(request, poll_id):
    """
    Renders the poll_detail.html template which allows a user to vote
    on the choices of a poll.
    """
    # poll = Poll.objects.get(id=poll_id)
    poll = get_object_or_404(Poll, id=poll_id)

    context = { 'poll': poll }
    return render(request, 'polls/poll_detail.html', context)

@login_required
def poll_vote(request, poll_id):
    # try:
    poll = get_object_or_404(Poll, id=poll_id)
    choice_id = request.POST.get('choice')
    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        choice.votes += 1
        choice.save()
    else:
        messages.error(request, 'No choice was found.')
        return HttpResponseRedirect(reverse('polls:detail', args=(poll_id,)))

    return render(request, 'polls/poll_results.html', {'poll': poll})
