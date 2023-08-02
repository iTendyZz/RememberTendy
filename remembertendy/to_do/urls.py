from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index_page, name='homepage'),
    path('signup/', views.signup_user, name='signuppage'),
    path('signin/', views.signin_user, name="signinpage"),
    path('logout/', views.logout_user, name="logoutpage"),
    path('to-do/add/', views.to_do_maker, name='addtodo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
