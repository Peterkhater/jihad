# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Project, Person

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at 

class PersonSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Person.objects.all() 
