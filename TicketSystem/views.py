from django.shortcuts import render
from .models import Ticket


def triage(request):
    tickets = Ticket.objects.all()

    return render(request, 'triage/master.html', {'tickets': tickets})


def pending(request):
    if request.method == "POST":
        return render(request, 'ticket/CreateTicket.html')
    if request.method == "GET":
        pending_tickets = Ticket.objects.filter(status='P')
        return render(request, 'triage/pending.html', {'tickets': pending_tickets})


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


def create_ticket_post(request, id):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'triage/master.html')


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


def update_ticket(request, id):
    if request.method == 'POST':
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
            'requestNote': 'I have no idea what i am doing'
        }
        return render(request, 'triage/master.html', context)