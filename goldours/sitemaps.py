from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from goldours_home.models import Blog


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return [
            'goldours_home:goldours-home',
            'goldours_home:about-goldours',
            'goldours_home:contact',
            'goldours_home:blogs',
            'goldours_home:all-services',
            'goldours_home:bbbee-consulting-and-training',
            'goldours_home:talent-management-and-development',
            'goldours_home:governance-and-direction',
            'goldours_home:systems-reviews-and-assurance',
            
        ]

    def location(self, item):
        return reverse(item)

 
class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('goldours_home:details-blog', args=[obj.slug])
