from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http import HttpResponse
import logging, mimetypes
from accounts.models import AboutCompany, CompanyCommunication

logger = logging.getLogger("accounts")

def download_profile(request):
    company = AboutCompany.objects.first()
    
    if company:
        try:
            file_path = company.company_profile.path
            file_name = company.company_profile.name
            if file_path and file_name:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    mime_type, _ = mimetypes.guess_type(file_path)
                    mime_type = mime_type or 'application/octet-stream'
                    response = HttpResponse(file_data, content_type=mime_type)
                    
                response['Content-Disposition'] = f'attachment; filename="{file_name.split("/")[-1]}"'
        
            return response
        except Exception as ex:
            logger.error("Missing company profile")
            messages.error(request, "Company profile not aploaded yet, send us an email if you have questions")
            return redirect("goldours_home:contact")
        
def communications(request):
    communications = CompanyCommunication.objects.all()
    context = {
        "communications": communications,
    }
    return render(request, "communications/communications.html", context)

def communication_detail(request, slug):
    communication = get_object_or_404(CompanyCommunication, slug=slug)
    images = communication.images.all()

    context = {
        "com": communication,
        "images": images
    }
    return render(request, "communications/communication_detail.html", context)
