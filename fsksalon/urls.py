from django.urls import path
from .views import (
    home,
    about,
    portfolio,
    HairView,
    HairDetailView,
    blogView,
    blogDetailView,
    courseView,
    courseDetailView,
    beautyView,
    beautyDetailView,
    bridalView, 
    tattooView, 
    nailView,
)

app_name = 'fsksalon'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('hair/', HairView.as_view(), name='hair'),
    path('blog/', blogView.as_view(), name='blog'),
    path('course/', courseView.as_view(), name='course'),
    path('beauty/', beautyView.as_view(), name='beauty'),
    path('bridal/', bridalView.as_view(), name='bridal'),
    path('tattoo/', tattooView.as_view(), name='tattoo'),
    path('nail/', nailView.as_view(), name='nail'),
    path('beauty-detail/<slug>/', beautyDetailView.as_view(), name='beauty-detail'),
    path('course-detail/<slug>/', courseDetailView.as_view(), name='course-detail'),
    path('blog-detail/<slug>/', blogDetailView.as_view(), name='blog-detail'),
    path('hair-detail/<slug>/', HairDetailView.as_view(), name='hair-detail'),
]