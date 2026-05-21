from rest_framework.routers import DefaultRouter
from .views_api import IntervencionViewSet

router = DefaultRouter()
router.register(r"intervenciones", IntervencionViewSet, basename="api-intervenciones")
urlpatterns = router.urls 