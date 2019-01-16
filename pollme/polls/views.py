from django.shortcuts import get_object_or_404, render
from .models import Poll

def polls_list(request):
    """
    Renders the polls_list.html template which lists all the 
    currently available polls.
    """
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)

def poll_detail(request, poll_id):
    """
    Renders the poll_detail.html template which allows a user to vote
    on the choices of a poll.
    """
    poll = get_object_or_404(Poll, id=poll_id)
    context = { 'poll': poll }
    return render(request, 'polls/poll_detail.html', context)
