from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

def all_service(request):
    return render(request, "services/all-services.html")

def bbbee_consulting_and_training(request):
    return render(request, "services/bbbee-consulting-and-training.html")

def governance_and_direction(request):
    return render(request, "services/governance-and-direction.html")

def systems_reviews_and_assurance(request):
    return render(request, "services/systems-reviews-and-assurance.html")

def talent_management_and_development(request):
    return render(request, "services/talent-management-and-development.html")