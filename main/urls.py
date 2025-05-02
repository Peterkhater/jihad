from django.urls import path
from .views import main,person,project_detail

urlpatterns = [
    path('', main,name='main'),
    path('morashah/<int:id>',person,name='person'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'),
]