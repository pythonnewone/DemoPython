from.import views

from django.urls import path

urlpatterns = [

    path('',views.fun,name='demo'),
    # path('add/',views.addition,name='addition')
    # path('about1/',views.about1,name='about1'),
    # path('contact/',views.contact,name='contact')

]