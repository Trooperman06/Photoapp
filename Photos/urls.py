from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('profile', views.profile, name="profile"),
    path('savedcontent', views.Saved_Content, name="Saved_Content"),
    path('AccountSettings', views.Account, name="Account_Settings"),

]
