from django.urls import path
from .import views

urlpatterns = [
    path('',views.HomepageView,name="home"),
    path('room/<str:pk>/',views.RoompageView,name="room"),
    path('room_create/',views.RoomCreateView,name="roomcreate_page"),
    path('room_update/<str:pk>/',views.updateroom,name="roomupdate_page"),
    path('room_delete/<str:pk>/',views.deleteviews,name="roomdelete_page"),

]
