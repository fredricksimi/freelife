from django.urls import path
from . import views

app_name= 'mainapp'
urlpatterns=[
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('center', views.center_view, name='center'),
    path('messages', views.messages_view, name='messages'),
    path('messages/<int:id>/', views.messages_detail_view, name='messagedetail'),
    path('contact', views.contact_view, name='contact'),

    #CRUD FUNCTIONALITY
    path('addcenter', views.add_center, name='addcenter'),
    path('edit/<int:cent_id>/', views.edit_center, name='editcenter'),
    path('delete/<int:cent_id>/', views.delete_center, name='deletecenter')
]