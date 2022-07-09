#two main things needed in urls page: path function and the urlpatterns which is a list. 

from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]