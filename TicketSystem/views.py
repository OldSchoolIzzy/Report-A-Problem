import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
        user = User.objects.get(username=request.POST['requester'])
        ticket = Ticket(subject=request.POST['subject'],
                        username_id=user.id,
                        dateCreated=datetime,
                        priority=request.POST['priority'],
                        buildingName=request.POST['building'],
                        status=request.POST['option'],
                        description=request.POST['note'])
        ticket.save()
        return redirect('http://127.0.0.1:8000/triage/')
    else:
        return render(request, 'ticket/CreateTicket.html')


def create_ticket_post(request, id):
    if request.method == "POST":
        return render(request, 'triage/master.html')


def view_ticket(request, ticket_id):
    if request.method == 'POST':
        ticket = Ticket.objects.get(pk=ticket_id)
        subject = request.POST['subject']
        priority = request.POST['priority']
        building = request.POST['building']
        option = request.POST['option']
        ticket.subject = subject
        ticket.buildingName = building
        ticket.status = option
        ticket.priority = priority
        ticket.save()
        return redirect('http://127.0.0.1:8000/triage/')
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket/viewTicket.html', {'ticket': ticket, 'options': ticket.STATUS_TYPES})


def update_ticket(request, id):
    if request.method == 'POST':
        return render(request, 'triage/master.html', )
