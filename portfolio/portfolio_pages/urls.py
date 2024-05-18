from portfolio.portfolio_pages import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home-page'),
    path('skills/', views.skills, name='skills-page'),
    path('projects/', views.projects, name='projects-page'),
    path('contact/', views.contact, name='contact-page'),
]
