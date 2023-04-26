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

        return render(request, 'ticket/CreateTicket.html', )
    if request.method == "GET":
        unsolved_tickets = Ticket.objects.filter(status='U')
        return render(request, 'triage/unsolved.html', {'tickets': unsolved_tickets})


def solved(request):
    if request.method == "POST":

        return render(request, 'ticket/CreateTicket.html', )
    if request.method == "GET":
        solved_tickets = Ticket.objects.filter(status='S')
        return render(request, 'triage/solved.html', {'tickets': solved_tickets})


def open_ticket(request):
    if request.method == "POST":

        return render(request, 'ticket/CreateTicket.html', )
    if request.method == "GET":
        open_tickets = Ticket.objects.filter(status='O')
        return render(request, 'triage/open.html', {'tickets': open_tickets})


def create_ticket(request):
    if request.method == "POST":

        return render(request, 'triage/master.html')
    else:
        return render(request, 'ticket/CreateTicket.html')


def create_ticket_post(request, id):
    if request.method == "POST":
        return render(request, 'triage/master.html')


def view_ticket(request, ticket_id):
    if request.method == 'POST':
        # update ticket in the database
        return
    ticket = Ticket.objects.get(id=ticket_id)

    print(ticket)
    return render(request, 'ticket/viewTicket.html', {'ticket': ticket, 'options': ticket.STATUS_TYPES})


def update_ticket(request, id):
    if request.method == 'POST':

        return render(request, 'triage/master.html', )
