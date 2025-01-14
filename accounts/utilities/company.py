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
        "mission": company.mission

    }
except:

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
        "mission": None

    }

def generate_order_number(model) -> str:
    order_id_start = f'BBGI{timezone.now().year}{timezone.now().month}'
    queryset = model.objects.filter(order_id__iexact=order_id_start).count()
      
    count = 1
    order_id = order_id_start
    while(queryset):
        order_id = f'BBGI{timezone.now().year}{timezone.now().month}{count}'
        count += 1
        queryset = model.objects.all().filter(order_id__iexact=order_id).count()

    return order_id