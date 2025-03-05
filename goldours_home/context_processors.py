from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from accounts.utilities.company import COMPANY
from goldours_home.models import BlogCategory, Blog, Review, TeamSummary

def global_context(request):
    PROTOCOL = "https" if request.is_secure() else "http"
    DOMAIN = get_current_site(request).domain

    context = {
        'domain' : DOMAIN,
        'protocol': PROTOCOL,
        'footerposts': Blog.objects.order_by("-created")[:2],
        "blog_categories": BlogCategory.objects.all(),
        "reviews": Review.objects.all(),
        "team": TeamSummary.objects.filter(slug="our-team-summary").first(),
        "facebook": COMPANY["facebook"],
        "instagram": COMPANY["instagram"],
        "linkedin": COMPANY["linkedin"],
        # "youtube": COMPANY["youtube"],
        "twitter": COMPANY["twitter"],
        "number": COMPANY["phone"],
        "emailinfo": COMPANY["company_support_mail"], 
        "address": COMPANY["address"],
        
        "vision": COMPANY["vision"],
        "mission": COMPANY["mission"],
        "clients": COMPANY["clients"],
        "projects": COMPANY["projects"],
        "experts": COMPANY["experts"],
        "media": COMPANY["media"],
        'GOOGLE_ANALYTICS_MEASUREMENT_ID': getattr(settings, 'GOOGLE_ANALYTICS_MEASUREMENT_ID', None),
        "site_key": getattr(settings, 'RECAPTCHA_ENTERPRISE_SITE_KEY', None),
        "project_id": getattr(settings, 'RECAPTCHA_ENTERPRISE_PROJECT_ID', None),
    }

    

    return context