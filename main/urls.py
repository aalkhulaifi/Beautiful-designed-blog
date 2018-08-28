from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('delete/<int:article_id>/', views.delete, name='delete'),
    path('update/<int:article_id>/', views.update, name='update'),
    path('likes/<int:article_id>/', views.likes, name="likes"),

    ]