# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
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

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ['main']  

    def location(self, item):
        return reverse(item)