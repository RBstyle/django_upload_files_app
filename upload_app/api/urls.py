from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("upload/", views.upload_file),
    path("files/", views.get_files),
]
