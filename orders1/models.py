from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('customizable', 'Customizable'),
        ('quantity', 'Quantity'),
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500 , null=True, blank=True)
    type = models.CharField(max_length=100 , choices = PRODUCT_TYPE_CHOICES)
    image = models.ImageField(upload_to = 'product/' , null=True, blank=True)

    def __str__(self):
        return self.name

class CustomizationCategory(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="customization_categories")

    def __str__(self):
        return f"{self.name} ({self.product.name})"

class Customization(models.Model):
    category = models.ForeignKey(CustomizationCategory, on_delete=models.CASCADE, related_name="customizations")
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.category.name}"

class Table(models.Model):
    number = models.IntegerField()
    status = models.CharField(max_length=100 , default = 'Progress')

    def __str__(self):
        return f"{self.number}"

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100 , default = 'Progress')

    def __str__(self):
        return f"{self.table.number} - {self.table.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    customization = models.ForeignKey(Customization, on_delete=models.CASCADE,null = True , blank = True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

class OrderItemCustomization(models.Model):
    orderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    customization = models.ForeignKey(Customization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customization} - {self.orderItem.product.name}"

class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    subtotal = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.name} - {self.order.category.name}"