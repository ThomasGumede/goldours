from django.urls import path
from .views.company import communication_detail, download_profile, communications
app_name = "accounts"
urlpatterns = [
    path("company/company-profile", download_profile, name="company-profile"),
    path("communication/<slug:slug>/", communication_detail, name="company_communication_detail"),
    path("communications", communications, name="communications"),
]

