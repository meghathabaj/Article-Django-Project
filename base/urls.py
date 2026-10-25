from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('sports/', sports, name='sports'),
    path('international/', international, name='international'),
    path('blogs/', blogs, name='blogs'),
    path('about/', about, name='about'),
    path('read/<int:id>',read,name='read')

]
