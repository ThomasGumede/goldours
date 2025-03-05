from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete, post_save
from accounts.utilities.abstracts import AbstractCreate, AbstractProfile
from accounts.utilities.choices import TITLE_CHOICES, RoleChoice
from accounts.utilities.file_handlers import handle_profile_upload
from accounts.utilities.validators import validate_fcbk_link, validate_in_link, validate_insta_link, validate_twitter_link, verify_rsa_phone
PHONE_VALIDATOR = verify_rsa_phone()

class Account(AbstractUser, AbstractProfile):
    profile_image = models.ImageField(help_text=_("Upload profile image"), upload_to=handle_profile_upload, null=True, blank=True)
    title = models.CharField(max_length=30, choices=TITLE_CHOICES)
    maiden_name = models.CharField(help_text=_("Enter your maiden name"), max_length=300, blank=True, null=True)
    occupation = models.CharField(default='N/A',help_text=_("Enter your current employment"), max_length=500, blank=True, null=True)
    biography = models.TextField(blank=True)
    professional_affiliations = models.CharField(default='N/A',help_text=_("Enter your professional affiliations"), max_length=700, blank=True, null=True)
    role = models.CharField(max_length=100, choices=RoleChoice.choices, default=RoleChoice.ALL)
    is_technical = models.BooleanField(default=False)
    is_email_activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["-created"]

    def __str__(self):
        return self.username

    def get_full_name(self):
        if self.title:
            return f"{self.title} {self.first_name[0]} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"
        
    def get_absolute_url(self):
        return reverse("accounts:user-details", kwargs={"username": self.username})

class AboutCompany(AbstractCreate):
    title = models.CharField(max_length=300, null=True, blank=True, unique=True)
    slogan = models.CharField(max_length=300, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=300, default="about-goldours-model", unique=True)
    operating_hours = models.CharField(max_length=300, null=True, blank=True, unique=True)
    address = models.CharField(max_length=300, null=True, blank=True, unique=True, help_text="Add company main address e.g Central park, KZN, 7441")
    address_coordinates = models.CharField(max_length=300, null=True, blank=True, help_text="Add company main address coordinates separated by comma e.g 10.00,12.66")
    number_of_clients = models.IntegerField(default=0)
    number_of_projects_completed = models.IntegerField(default=0)
    number_of_skilled_experts = models.IntegerField(default=0)
    number_of_media_activities = models.IntegerField(default=0)
    phone = models.CharField(help_text=_("Enter telephone number"), max_length=15, validators=[PHONE_VALIDATOR], unique=True, null=True, blank=True)
    alternate_phone = models.CharField(help_text=_("Enter other telephone number"), max_length=15, validators=[PHONE_VALIDATOR], unique=True, null=True, blank=True)
    facebook = models.URLField(validators=[validate_fcbk_link], blank=True, null=True, help_text=_("Enter facebook link e.g https://www.facebook.com/profile"))
    twitter = models.URLField(validators=[validate_twitter_link], blank=True, null=True, help_text=_("Enter twitter link e.g https://www.twitter.com/profile"))
    instagram = models.URLField(validators=[validate_insta_link], blank=True, null=True, help_text=_("Enter instagram link e.g https://www.instagram.com/profile"))
    linkedIn = models.URLField(validators=[validate_in_link], blank=True, null=True, help_text=_("Enter linkedin link e.g https://www.linkedin.com/profile"))
    email = models.EmailField(null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    vision = models.TextField(blank=True, null=True, unique=True)
    mission = models.TextField(blank=True, null=True, unique=True)
    company_profile = models.FileField(help_text=_("Upload company profile"), upload_to=handle_profile_upload, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'About Company'
        verbose_name_plural = 'About Companys'