from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', MenuItemsView.as_view(), name="menu"),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name="single-menu-item")
]
