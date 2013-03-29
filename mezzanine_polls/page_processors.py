from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import Poll, Vote, Choice
from .forms import VotingForm


@processor_for(Poll)
def voting_form(request, page):
    '''
    Processor for the poll page.
    '''

    poll_users = [
        v.user
        for v in
        Vote.objects.filter(choice__poll=page.poll)
    ]
    total_votes = len(poll_users)

    poll_choices = [
        (c.id, c.text)
        for c in
        page.poll.choice_set.all()
    ]

    if request.user in poll_users:
        # render results
        poll_results = [
            (
                c.text,
                c.vote_set.count(),
                (c.vote_set.count() * 100) / total_votes
            )
            for c in
            page.poll.choice_set.all()
        ]
        return {'poll_results': poll_results}
    else:
        if request.method == 'POST':
            # process vote
            print(request.POST)
            form = VotingForm(request.POST, poll_choices=poll_choices)
            if form.is_valid():
                # Get choice id
                choice_id = form.cleaned_data['choices']
                choice = Choice.objects.get(id=choice_id)
                vote = Vote(choice=choice, user=request.user)
                vote.save()
                return HttpResponseRedirect(page.get_absolute_url())
            else:
                return {'form': form}
        form = VotingForm(poll_choices=poll_choices)
        return {'form': form}
