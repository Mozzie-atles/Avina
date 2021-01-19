from .views import ItemView, ItemDetail, Userlist, UserDetails, CreateItemView
from django.urls import path


urlpatterns = [
    path("items", ItemView.as_view()),
    path("items/create", CreateItemView.as_view()),
    path("items/<int:pk>", ItemDetail.as_view()),
    path("users/", Userlist.as_view()),
    path("users/<int:pk>", UserDetails.as_view())

]
