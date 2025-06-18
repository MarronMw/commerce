from django.db import models  # type: ignore

# Create your models here.


class Category(models.Model):
    category_No = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_No = models.CharField(max_length=12, primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, default="default.png")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 default="default"
                                 )
    product_colour = models.CharField(max_length=30)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    customer_No = models.CharField(max_length=50, primary_key=True)
    customer_name = models.CharField(max_length=55)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=100,)
    password = models.CharField(max_length=16, null=False)
    shipping_address = models.CharField(max_length=60)
    contact = models.CharField(max_length=14)
    image = models.ImageField(default="default.png", blank=True,upload_to='profile_pics/')

    def __str__(self):
        return self.customer_name


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=30)

    def __str__(self):
        return self.status_name


class Order(models.Model):
    order_No = models.CharField(max_length=12, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_Date = models.DateField(auto_now=True)
    order_Status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    total_Price = models.IntegerField()

    def __str__(self):
        return self.customer.customer_name+self.order_No


class OrderItem(models.Model):
    orderItem_No = models.CharField(
        primary_key=True, max_length=12, blank=True)
    order_No = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_No = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_order_time = models.IntegerField()


class Cart(models.Model):
    customer_No = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_No = models.ForeignKey(Product, on_delete=models.CASCADE)
