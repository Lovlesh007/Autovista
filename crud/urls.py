from rest_framework import routers
from .api import CrudViewSet

router = routers.DefaultRouter()
router.register('api/crud',CrudViewSet,'crud')

urlpatterns = router.urls
