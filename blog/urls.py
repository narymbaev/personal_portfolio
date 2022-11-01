from django.urls import path
from .views import blogs, detail

app_name = 'blog'

urlpatterns = [
    path('', blogs, name='blogs'),
    path('<int:pk>', detail, name='detail'),
]