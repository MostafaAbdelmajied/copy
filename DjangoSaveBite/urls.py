"""
URL configuration for DjangoSaveBite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from numpy.ma.tests.test_mrecords import TestView

from api.views import EmbedDataView, ExtractDataView, TestProjectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('embed/', EmbedDataView.as_view(), name='embed_data'),
    path('extract/', ExtractDataView.as_view(), name='extract_data'),
    path('test/', TestProjectView.as_view(), name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

