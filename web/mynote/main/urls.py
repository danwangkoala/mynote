
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('add_note/', views.add_note, name='add_note')
]