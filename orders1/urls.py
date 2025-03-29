from django.urls import path,include
from rest_framework import routers
from orders1.views import *

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customization', CustomizationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'tables',TableViewSet)
router.register(r'invoice',InvoiceViewSet)
router.register(r'orderitem_customizations',OrderItemCustomizationViewSet)
router.register(r'customization_category',CustomizationCategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]