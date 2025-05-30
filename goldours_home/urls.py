from django.urls import path
from goldours_home.views.media_views import media_details, download_media_file, media_files
from goldours_home.views.services import all_service, bbbee_consulting_and_training, talent_management_and_development, systems_reviews_and_assurance, governance_and_direction
from goldours_home.views.admin_views import all_accounts
from goldours_home.views.blog_views import all_blogs, blog_details, blogs, create_blog, delete_blog, update_blog
from goldours_home.views.home import about_goldours, contact, dashboard, test_400, home, privacy, cookie, search, terms_and_conditions, contact_ajax
from goldours_home.views.member_views import create_member, delete_member, team_member_details, team_members, update_member

app_name = 'goldours_home'
urlpatterns = [
    path("", home, name="goldours-home"),
    path("about-us/", about_goldours, name="about-goldours"),
    path("about-us/teams/<member_id>", team_member_details, name="team-member"),
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
    path("articles/<slug:category_slug>/", blogs, name="blogs-by-category"),
    path("media-and-pictures/", media_files, name="media-files"),
    path("media-and-pictures/<slug:media_slug>", media_details, name="media-details"),
    path("media-and-pictures/files/<slug:media_slug>", download_media_file, name="media-file-download"),
    path("dashboard/accounts", all_accounts, name="all-accounts"),
    path("dashboard/blogs", all_blogs, name="all-blogs"),
    path("dashboard/blogs/create", create_blog, name="create-blog"),
    path("article/<slug:post_slug>", blog_details, name="details-blog"),
    path("dashboard/blogs/update/<slug:post_slug>", update_blog, name="update-blog"),
    path("dashboard/blogs/delete/<slug:post_slug>", delete_blog, name="delete-blog"),

    path("dashboard/members", team_members, name="team-members"),
    path("dashboard/member/create", create_member, name="create-member"),
    path("dashboard/member/update/<member_id>", update_member, name="update-member"),
    path("dashboard/member/delete/<member_id>", delete_member, name="delete-member"),
]
