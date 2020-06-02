"""hatcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include

from rest_framework import permissions
from rest_framework_nested.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from tabulation.views import HatchViewSet

schema_view = get_schema_view(
    openapi.Info(title="Broadcast Backend API", default_version="v1", description="Broadcast Backend API",),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from rest_framework_nested.routers import DefaultRouter
router = DefaultRouter()

hatchviewupdate = HatchViewSet.as_view({'put': 'update'})
hatchviewlist = HatchViewSet.as_view({'get': 'list'})
hatchviewdetail = HatchViewSet.as_view({'get': 'retrieve'})
hatchviewcreate = HatchViewSet.as_view({'post': 'create'})
HatchViewfreelist = HatchViewSet.as_view({'get': 'free'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('hatchrecords/', hatchviewlist, name="hatchrecords"),
    path('hatchrecordsfree/', HatchViewfreelist, name="hatchrecords_free"),
    path('hatchrecords/<pk>/detail', hatchviewdetail, name="hatchrecords_deatail"),
    path('hatchrecords/create/', hatchviewcreate, name="hatchrecords_create"),
    path('hatchrecords/<pk>/update', hatchviewupdate, name="hatchrecords_update"),
]


