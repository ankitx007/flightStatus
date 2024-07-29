from django.db import models

class Subscriber(models.Model):
    flight_number = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    opt_in = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight_number} - {self.email or self.phone_number}"
