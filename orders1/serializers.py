from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CustomizationSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Customization
        fields = '__all__'

class CustomizationCategorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='pro``duct.name', read_only=True)
    customizations = CustomizationSerializer(many=True, read_only=True)

    class Meta:
        model = CustomizationCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    customization_categories = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_customization_categories(self, product):
        if product.type == 'customizable':
            return CustomizationCategorySerializer(product.customization_categories.all(), many=True).data
        return None

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    table_number = serializers.IntegerField(source='table.number', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    customization_name = serializers.CharField(source='customization.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderItemCustomizationSerializer(serializers.ModelSerializer):
    customization_name = serializers.CharField(source='customization.name', read_only=True)

    class Meta:
        model = OrderItemCustomization
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id', read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
