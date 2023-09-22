from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("upload/", views.AddFile.as_view()),
    path("files/", views.get_files),
]
