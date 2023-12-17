from django.urls import path
from box.views import(
  ListAllViews,
  ListMyBoxView,
  BoxCreateView,
  BoxUpdateView,
  DestroyBoxView)

urlpatterns = [
    path("list-all-boxes", ListAllViews.as_view(), name="list-all-boxes"),
    path("create-box", BoxCreateView.as_view(), name="create-box"),
    path("update-box/<int:pk>", BoxUpdateView.as_view(), name="update-box"),
    path("list-my-boxes", ListMyBoxView.as_view(), name="list-my-boxes"),
    path("delete-box/<int:pk>", DestroyBoxView.as_view(), name="delete-box"),
  ]
  