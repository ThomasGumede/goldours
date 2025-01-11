from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from accounts.utilities.company import COMPANY
from goldours_home.models import BlogCategory, Blog

def global_context(request):
    PROTOCOL = "https" if request.is_secure() else "http"
    DOMAIN = get_current_site(request).domain

    context = {
        'domain' : DOMAIN,
        'protocol': PROTOCOL,
        'footerposts': Blog.objects.order_by("-created")[:2],
        "blog_categories": BlogCategory.objects.all(),
        "facebook": COMPANY["facebook"],
        "instagram": COMPANY["instagram"],
        "linkedin": COMPANY["linkedin"],
        # "youtube": COMPANY["youtube"],
        # "tiktok": COMPANY["tiktok"],
        "company_support": COMPANY["phone"],
        "company_support_mail": COMPANY["company_support_mail"], 
        "address": COMPANY["address"],
        "company_city": COMPANY["company_city"],
        "company_state": COMPANY["company_state"],
        "company_zipcode": COMPANY["company_zipcode"],
        "vision": COMPANY["vision"],
        "mission": COMPANY["mission"],
        'GOOGLE_ANALYTICS_MEASUREMENT_ID': getattr(settings, 'GOOGLE_ANALYTICS_MEASUREMENT_ID', None)
    }

    

    return context