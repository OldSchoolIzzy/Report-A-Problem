from django.shortcuts import render


def triage(request):
    # load newly create tickets in the database here
    return render(request, 'triage/master.html')


def pending(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        return render(request, 'triage/pending.html')


def unsolved(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        return render(request, 'triage/unsolved.html')


def solved(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        return render(request, 'triage/solved.html')


def open_ticket(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    if request.method == "GET":
        return render(request, 'triage/open.html')


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