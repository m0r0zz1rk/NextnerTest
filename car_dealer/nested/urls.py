from django.urls import path

from nested.views import StartPageView, EditAutoView

urlpatterns = [
    path('', StartPageView.as_view(), name="start"),
    path('edit/<int:pk>', EditAutoView.as_view(), name="edit_auto")
]