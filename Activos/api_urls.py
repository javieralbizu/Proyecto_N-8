from rest_framework.routers import DefaultRouter 
from .views_api import ActivoViweSet

router = DefaultRouter() 
router.register(r'activos', ActivoViweSet, basename='api-activos') 
urlpatterns = router.urls 