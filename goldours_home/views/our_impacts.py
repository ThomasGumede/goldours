import logging
from django.shortcuts import render


def get_team(request):
    return render(request, 'impacts/team.html')

def get_clients(request):
    return render(request, 'impacts/clients.html')

def get_accreditations(request):
    return render(request, 'impacts/accreditations.html')

def get_contributions(request):
    return render(request, 'impacts/contributions.html')

def get_testimonials(request):
    return render(request, 'impacts/testimonials.html')