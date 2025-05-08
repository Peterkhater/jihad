from django.shortcuts import render
from .models import Project, Category, Person, Gallery,MySetting
from django.shortcuts import get_object_or_404

def main(request):
    projects = Project.objects.select_related('category').all()
    categories = Category.objects.all()
    persons = Person.objects.all()
    gallery = Gallery.objects.all()
    setting = MySetting.objects.last()
    context = {
        'projects': projects,
        'categories': categories,
        'persons': persons,
        'gall': gallery,
        'setting':setting,
    }
    return render(request, 'main.html', context)

def person(request,id):
    person = get_object_or_404(Person, id=id)
    setting = MySetting.objects.last()
    category = Category.objects.all()
    return render(request,'person.html',{'person': person,'setting':setting,'cat':category,})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)
    setting = MySetting.objects.last()
    

    context = {
        'project': project,
        'related_projects': related_projects,
        'setting':setting
    }
    return render(request, 'detail.html', context)

# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)