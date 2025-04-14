from goldours_home.models import Media, BlogCategory
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
import logging, mimetypes

logger = logging.getLogger("accounts")

def media_files(request, category_slug=None):
    query = request.GET.get("query", None)
    template = "medias/media-files.html"
    model = Media
    
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        blogs = model.objects.filter(category=category)
        if query:
            blogs = blogs.order_by('-created').filter(title__icontains=query)
    else:
        blogs = model.objects.order_by('-created')
        if query:
            blogs = blogs.filter(title__icontains=query)

    context = {"posts": blogs, "query": query}

    return render(request, template, context)

def download_media_file(request, media_slug):
    media = get_object_or_404(Media.objects.select_related("category"), slug=media_slug)
    
    
    try:
            file_path = media.mediafile.path
            file_name = media.mediafile.name
            if file_path and file_name:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    mime_type, _ = mimetypes.guess_type(file_path)
                    mime_type = mime_type or 'application/octet-stream'
                    response = HttpResponse(file_data, content_type=mime_type)
                    
                response['Content-Disposition'] = f'attachment; filename="{file_name.split("/")[-1]}"'
        
            return response
    except Exception as ex:
        logger.error("Missing Media file")
        messages.error(request, "Media file not aploaded yet, send us an email if you have questions")
        return redirect("goldours_home:media-details", media_slug=media.slug)

def media_details(request, media_slug):
    
    media = get_object_or_404(Media.objects.select_related("category"), slug=media_slug)
    recent_posts = Media.objects.exclude(id = media.id).order_by("-created")[:5]

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         if request.user.is_authenticated:
    #             instance.commenter = request.user
    #         else:
    #             instance.commenter = None
    #         instance.post = blog
    #         instance.save()
    #         messages.success(request, "Comment added successfully")
    #         return redirect('goldours_home:details-blog', post_slug=blog.slug)
    #     else:
    #         messages.error(request, "Comment not added, fix errors below")
    #         return redirect('goldours_home:details-blog', post_slug=blog.slug)
        
    # form = CommentForm()
    return render(request, 'medias/media-details.html', {"post": media, "recent_posts": recent_posts})