from rest_framework.routers import DefaultRouter 
from .views_api import TecnicoViweSet

router = DefaultRouter() 
router.register(r'tecnicos', TecnicoViweSet, basename='api-tecnicos') 
urlpatterns = router.urls 