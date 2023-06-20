from . import views
from django.urls import path


urlpatterns = [

    path('',views.home,name='home'),
    path('form',views.form,name='form'),
    path('order_conform',views.order_conform,name="order_conform")
]
