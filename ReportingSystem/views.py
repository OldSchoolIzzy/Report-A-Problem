from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from TicketSystem.models import Ticket


def home(request):
    return render(request, "LandingPage.html")
def issues(request):
    return render(request, "Issue.html")
def cleaniness(request):
    return render(request,"Cleaniness.html")

def electrical(request):
    return render(request,"Electrical.html")

def hazards(request):
    return render(request,"Hazards.html")

def hvac(request):
    return render(request,"HVAC.html")

def it(request):
    return render(request,"IT.html")

def pest(request):
    return render(request,"Pest.html")

def plumbing(request):
    return render(request,"Plumbing.html")

def restroom(request):
    return render(request,"Restroom.html")

def ticket(request):
    return render(request,"tickt.html")
def create_ticket_2(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST['requester'])
        filepath = request.FILES['image'] if 'image' in request.FILES else False
        if filepath is not False:
            ticket = Ticket(subject=request.POST['subject'],
                            username_id=user.id,
                            dateCreated=datetime,
                            buildingName=request.POST['building'],

                            description=request.POST['note'],
                            image=request.FILES['image'],
                            issue=request.POST['issue'],
                            room=request.POST['room'])



            ticket.save()
            return redirect('http://127.0.0.1:8000/system/ticket')
        ticket = Ticket(subject=request.POST['subject'],
                        username_id=user.id,
                        dateCreated=datetime,
                        buildingName=request.POST['building'],

                        issue=request.POST['issue'],
                        description=request.POST['note'],
                        room=request.POST['room'])
        ticket.save()
        return redirect('http://127.0.0.1:8000/system/ticket')

# def create_ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST, request.FILES)
#         if form.is_valid():
#             ticket = form.save()
#             return redirect('ticket_list')
#     else:
#         form = TicketForm()
#
#     return render(request, 'create_ticket.html', {'form': form})

# def ticket_list(request):
#     tickets = Ticket.objects.all()
#     return render(request, 'ticket_list.html', {'tickets': tickets})


