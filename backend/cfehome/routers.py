from posixpath import basename
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
# router.register('products_rout', ProductViewSet, basename='products')
router.register('products_rout', ProductGenericViewSet, basename='products')

urlpatterns = router.urls