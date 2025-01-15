import logging
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from goldours_home.forms import EmailForm, SearchForm
from goldours_home.models import Blog, Member
from goldours_home.tasks import send_email_to_admin
from goldours_home.utilities.decorators import user_not_superuser_or_staff
from django.contrib.auth.decorators import login_required
from django.conf import settings

from goldours_home.utilities.recaptcha import validate_recaptcha

logger = logging.getLogger("tasks")

def home(request):
    blogs = Blog.objects.all()[:5]
    return render(request, "home/home.html", {"posts": blogs})

def about_goldours(request):
    members = Member.objects.all()
    blogs = Blog.objects.all()[:5]
    return render(request, "home/about-us.html", {"members": members, "posts": blogs})

def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recaptcha_token = form.cleaned_data.get('recaptcha_token')
            print(recaptcha_token)
            try:
                validate_recaptcha(
                    token=recaptcha_token,
                    project_id=settings.RECAPTCHA_ENTERPRISE_PROJECT_ID,
                    site_key=settings.RECAPTCHA_ENTERPRISE_SITE_KEY,
                )
                form.save()
                send_email_to_admin(form.cleaned_data["subject"], form.cleaned_data["message"], form.cleaned_data["from_email"], form.cleaned_data["name"])
                messages.success(request, "We have successfully receive your email, will be in touch shortly")
                return redirect("goldours_home:contact")
            
            except ValueError as e:
                logger.error(f"Failed to verify this due to f{e}")
                messages.success(request, "We have successfully receive your email, will be in touch shortly")
                return redirect("goldours_home:contact")
            
            
        else:
            messages.error(request, "Something went wrong, please fix errors below")
            for err in form.errors:
                messages.error(request, f"{err}")
                return redirect("goldours_home:contact")
            
    form = EmailForm()
    return render(request, "home/contact-us.html", {"form": form})




def contact_ajax(request):
    if request.method == 'POST':
        try:
            form = EmailForm(request.POST)
            if form.is_valid():
                form.save()
                send_email_to_admin(form.cleaned_data["subject"], form.cleaned_data["message"], form.cleaned_data["from_email"], form.cleaned_data["name"])
                messages.success(request, "We have successfully receive your email, will be in touch shortly")
                return JsonResponse({"success": True, "message": "We have successfully receive your email, will be in touch shortly"}, status=200)
            else:
                messages.error(request, "Something went wrong, please fix errors below")
                return JsonResponse({"success": True, "message": "Something went wrong, we couldn' receive your email"}, status=200)
        except Exception as ex:
            return JsonResponse({"success": True, "message": "Something went wrong, we couldn' receive your email"}, status=500)
            
    form = EmailForm()
    return render(request, "home/contact-us.html", {"form": form})

@login_required
@user_not_superuser_or_staff
def dashboard(request):
    
    users = get_user_model().objects.all()
    return render(request, "dashboard/dashboard.html", {"users": users})

def search(request):

    form = SearchForm()
    query = request.GET.get("query", None)
    query_by = request.GET.get("search_by", None)
    place = request.GET.get("place", None)
    if not query:
        return render(request, "home/search.html")
    
    results_dic = {
        "news": Blog.objects.filter(Q(title__icontains=query)),
        }
    context = {}

    context["form"] = form
    
    return render(request, "home/search.html", context=context)

def terms_and_conditions(request):
    return render(request, "home/terms_and_conditions.html")

def privacy(request):
    return render(request, "home/privacy.html")

def refunds(request):
    return render(request, "home/refunds.html")

def faqs(request):
    blogs = Blog.objects.all()[:5]
    return render(request, "home/faqs.html", {"posts": blogs})
