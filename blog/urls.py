#
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import path, include
# #from users import views as user_views
# from . import views
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('register/', user_views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='users/logout.html'),
#     path('about/', views.about, name='blog-about'),
#     path('', include('blog.urls')),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]