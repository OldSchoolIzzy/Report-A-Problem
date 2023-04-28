from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Ticket


@login_required(login_url='/login')
def triage(request):
    tickets = Ticket.objects.all()

    return render(request, 'triage/master.html', {'tickets': tickets})


@login_required(login_url='/login')
def pending(request):
    if request.method == "POST":
        return render(request, 'ticket/CreateTicket.html')
    if request.method == "GET":
        pending_tickets = Ticket.objects.filter(status='P')
        return render(request, 'triage/pending.html', {'tickets': pending_tickets})


@login_required(login_url='/login')
def unsolved(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        unsolved_tickets = Ticket.objects.filter(status='U')
        return render(request, 'triage/unsolved.html', {'tickets': unsolved_tickets})


@login_required(login_url='/login')
def solved(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        solved_tickets = Ticket.objects.filter(status='S')
        return render(request, 'triage/solved.html', {'tickets': solved_tickets})


@login_required(login_url='/login')
def open_ticket(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        open_tickets = Ticket.objects.filter(status='O')
        return render(request, 'triage/open.html', {'tickets': open_tickets})


@login_required(login_url='/login')
def create_ticket(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'triage/master.html')
    else:
        return render(request, 'ticket/CreateTicket.html')


@login_required(login_url='/login')
def create_ticket_post(request, id):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'triage/master.html')


@login_required(login_url='/login')
def view_ticket(request):
    if request.method == 'GET':
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
            'requestNote': 'I have no idea what i am doing'
        }
        return render(request, 'ticket/viewTicket.html', context)
    if request.method == 'UPDATE':
        # Update the ticket in the database
        return


@login_required(login_url='/login')
def update_ticket(request, id):
    if request.method == 'POST':
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
            'requestNote': 'I have no idea what i am doing'
        }
        return render(request, 'triage/master.html', context)
