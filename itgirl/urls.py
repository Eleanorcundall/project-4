"""
URL configuration for itgirl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home_feed.views import home_view, blog_post_detail_view, category_view
from user_submissions.views import submit_post

urlpatterns = [
    path('', include('home_feed.urls')),
    path('admin/', admin.site.urls),
    path('post/<slug>/', blog_post_detail_view, name='blog_post_detail'),
    path('category/<str:category>/', category_view, name='category_view'),
    path('accounts/', include('allauth.urls')),
    path('user_submissions/', include('user_submissions.urls', namespace='user_submissions')),
]
