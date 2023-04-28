from django.shortcuts import render

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

