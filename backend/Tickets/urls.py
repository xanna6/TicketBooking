from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'movieDetails', views.MovieDetailsViewSet, basename='Movie')
router.register(r'screening', views.ScreeningViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'customer', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
