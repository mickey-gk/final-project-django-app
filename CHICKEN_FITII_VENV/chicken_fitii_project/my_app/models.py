from django.contrib.auth.models import AbstractUser
from django.db import models

# MY MODELS:

# user model
class CustomUser(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add a related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Add a related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# model to help sellers list differnt types of chickens available for sell
class ChickenType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_seller': True})
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return self.name


# order model -for customer to make purchases
class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_buyer': True})
    chicken_type = models.ForeignKey(ChickenType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.chicken_type.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.buyer.username}"


# location model for sellers
class Location(models.Model):
    seller = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_seller': True})
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address}, {self.city}"
