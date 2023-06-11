from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('products/',views.index),
    path('login/',views.login),
    path('new/',views.new ),
    path('signup/',views.signup),
    path('comment/',views.comment),
    path('order/',views.order),
    path('load/',views.load),
]