from django.contrib import admin
from accounts.models import Account, AboutCompany
from .models import CompanyCommunication, CompanyCommunicationImage

class CommunicationImageInline(admin.TabularInline):
    model = CompanyCommunicationImage
    extra = 1

@admin.register(CompanyCommunication)
class CompanyCommunicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'created')
    prepopulated_fields = {"slug": ("title",)}  # You may remove if relying on auto slug
    inlines = [CommunicationImageInline]
    search_fields = ('title', 'location')
    list_filter = ('event_date',)
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    pass