from django.shortcuts import render


def triage(request):
    if request.method == "POST":
        context = {
            'requester': 'Israel Herrera',
            'Subject': 'My sink ran away',
            'request': request,
        }
        return render(request, 'ticket/CreateTicket.html', context)
    else:
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


def create_ticket(request):
    if request.method == "GET":
        return render(request, 'ticket/CreateTicket.html')
