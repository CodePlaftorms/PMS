from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('elearning/', views.elearning, name='elearning'),
    path('updatedkanban/', views.updatedkanban, name='updatedkanban'),
    path('template/', views.template, name='template'),
    path('logout/', views.logout, name='logout'),
    #path('updatedkanban/', views.updatedkanban, name='updatedkanban'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)