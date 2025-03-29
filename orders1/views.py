from rest_framework import viewsets
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    category_name = serializers.CharField(source='category.name', read_only=True)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomizationViewSet(viewsets.ModelViewSet):
    product_name = serializers.CharField(source='product.name', read_only=True)

    queryset = Customization.objects.all()
    serializer_class = CustomizationSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemCustomizationViewSet(viewsets.ModelViewSet):
    queryset = OrderItemCustomization.objects.all()
    serializer_class = OrderItemCustomizationSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class CustomizationCategoryViewSet(viewsets.ModelViewSet):
    queryset = CustomizationCategory.objects.all()
    serializer_class = CustomizationCategorySerializer
