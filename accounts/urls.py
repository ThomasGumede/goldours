from django.urls import path
from .views.company import download_profile
app_name = "accounts"
urlpatterns = [
    path("company/company-profile", download_profile, name="company-profile")
]
