from django.utils import timezone
from accounts.models import AboutCompany

try:
    company = AboutCompany.objects.get(slug="about-goldours-model")
    COMPANY = {
        "facebook": company.facebook,
        "twitter": company.twitter,
        "instagram": company.instagram,
        "linkedin": company.linkedIn,
        "website": "https://goldours.co.za",
        "company_support_mail": company.email,
        "phone": company.phone,
        "other_phone": company.alternate_phone,
        # "youtube": "https://www.youtube.com/@blackbusinessgrowthinitiat6153",
        "address": company.address,
        "vision": company.vision,
        "clients": company.number_of_clients,
        "projects": company.number_of_projects_completed,
        "experts": company.number_of_skilled_experts,
        "media": company.number_of_media_activities,
        "mission": company.mission

    }
except AboutCompany.DoesNotExist as ex:

    COMPANY = {
        "facebook": None,
        "twitter": None,
        "instagram": None,
        "linkedin": None,
        "website": "https://goldours.co.za",
        "company_support_mail": "info@goldours.co.za",
        "phone": "	+27 79 213 1566",
        "other_phone": '+27 21 525 9188',
        # "youtube": "https://www.youtube.com/@blackbusinessgrowthinitiat6153",
        "address": "Cape Town, 7441, RSA",
    
        "vision": None,
        "clients": 100,
        "projects": 50,
        "experts": 20,
        "media": 10,
        "mission": None

    }
