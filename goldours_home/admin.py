from django.contrib import admin
from goldours_home.models import BlogCategory, Blog, Comment, EmailModel, Privacy, Review, TeamSummary, Client, Accreditation, Media
from django.utils.html import format_html


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="35" style="border-radius:8px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"

    def status_colored(self, obj):
        # Example — if you later add a "status" field to Blog
        return format_html('<span style="color:green;font-weight:bold;">Published</span>')
    status_colored.short_description = "Status"
    
    list_display = ('title', 'category', 'author', 'image_preview', 'created', 'status_colored')
    list_filter = ('category', 'author')
    # filter_horizontal = ("tags",)
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview',)
    list_per_page = 20

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category', 'author')
        }),
        ('Details', {
            'fields': ('content', 'tags')
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
    )

    


class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = ("commenter", "created", "comment")
    extra = False

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(TeamSummary)
class TeamSummaryAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("label", )
    date_hierarchy = "created"
    empty_value_display = "Empty"
    prepopulated_fields = {"slug": ["label"]}


# @admin.register(Blog)
# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ["title"]}

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ["title"]}

@admin.register(EmailModel)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("subject", "from_email", "created")
    readonly_fields = ("subject", "from_email", "name", "phone", "message", "created")



