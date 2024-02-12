from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer:
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'Delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=10)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_not_add=True)
    updated_at = models.DateTimeField(auto_not=True)

    def __str__(self):
        return f"{self.name}"