from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'organizer', views.DevopsOrganizerViews, basename='organizer')

api_urlpatterns = router.urls
