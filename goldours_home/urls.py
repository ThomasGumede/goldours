from django.urls import path
from goldours_home.views.media_views import media_details, download_media_file, media_files
from goldours_home.views.services import all_service, bbbee_consulting_and_training, talent_management_and_development, systems_reviews_and_assurance, governance_and_direction
from goldours_home.views.admin_views import all_accounts
from goldours_home.views.blog_views import all_blogs, blog_details, blogs, create_blog, delete_blog, tinymce_image_upload, update_blog
from goldours_home.views.home import about_goldours, contact, course_details, dashboard, test_400, home, privacy, cookie, search, terms_and_conditions, contact_ajax
from goldours_home.views.our_impacts import get_accreditations, get_clients, get_team, get_testimonials, get_contributions

app_name = 'goldours_home'
urlpatterns = [
    path("", home, name="goldours-home"),
    path("about-us/", about_goldours, name="about-goldours"),
    path("about-us/asset-management-online-course", course_details, name="course-details"),
    path("contact-us/", contact, name="contact"),
    path("api/contact-us", contact_ajax, name="api-contact"),
    path("dashboard", dashboard, name="dashboard"),
    path("search", search, name="search"),
    path("goldours/test_400", test_400, name="faqs"),
    path("about-us/privacy-policy", privacy, name="policy"),
    path("about-us/cookie-policy", cookie, name="cookie"),
    path("services", all_service, name="all-services"),
    path("services/bbbee-consulting-and-training", bbbee_consulting_and_training, name="bbbee-consulting-and-training"),
    path("services/talent-management-and-development", talent_management_and_development, name="talent-management-and-development"),
    path("services/governance-and-direction", governance_and_direction, name="governance-and-direction"),
    path("services/systems-reviews-and-assurance", systems_reviews_and_assurance, name="systems-reviews-and-assurance"),
    path("about-us/terms-and-conditions", terms_and_conditions, name="terms"),
    path("articles/", blogs, name="blogs"),
    path("articles/category=<slug:category_slug>/", blogs, name="blogs-by-category"),
    path("articles/tag=<slug:tag_slug>/", blogs, name="blogs_by_tag"),
    path("articles//category=<slug:category_slug>/tag=<slug:tag_slug>/", blogs, name="blogs_by_category_tag"),
    path("media-and-pictures/", media_files, name="media-files"),
    path("media-and-pictures/<slug:media_slug>", media_details, name="media-details"),
    path("media-and-pictures/files/<slug:media_slug>", download_media_file, name="media-file-download"),
    path("dashboard/accounts", all_accounts, name="all-accounts"),
    path("dashboard/blogs", all_blogs, name="all-blogs"),
    path("dashboard/blogs/create", create_blog, name="create-blog"),
    path("article/<slug:post_slug>", blog_details, name="details-blog"),
    path("about-us/our-team", get_team, name='get-team'),
    path("about-us/our-contributions", get_contributions, name='get-contributions'),
    path("about-us/our-testimonials", get_testimonials, name='get-testimonials'),
    path("about-us/our-accreditations", get_accreditations, name='get-accreditations'),
    path("about-us/our-clients", get_clients, name='get-clients'),

    
    path('tinymce-upload/', tinymce_image_upload, name='tinymce_upload'),
]
