from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    """listView дя перечесления содержимого модели базы данных"""
    model = Post
    template_name = 'home.html'
# Create your views here.
