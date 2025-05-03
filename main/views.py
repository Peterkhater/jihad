from django.shortcuts import render
from .models import Project, Category, Person, Gallery
from django.shortcuts import get_object_or_404

def main(request):
    projects = Project.objects.select_related('category').all()
    categories = Category.objects.all()
    persons = Person.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'projects': projects,
        'categories': categories,
        'persons': persons,
        'gall': gallery,
    }
    return render(request, 'main.html', context)

def person(request,id):
    person = get_object_or_404(Person, id=id)
    return render(request,'person.html',{'person': person})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)
    
    context = {
        'project': project,
        'related_projects': related_projects
    }
    return render(request, 'detail.html', context)