from django.db import models
import datetime

# Create your models here.
class Message(models.Model):

    LOCATIONS=(

        ("Migori", "Migori"), ("Homabay", "Homabay"), ("Kisii", "Kisii"), ("Awendo", "Awendo")
    )
    REASONS=(

        ("Depression", "Depression"), ("Sexual Abuse", "Sexual Abuse"), ("Gender Based Violence", "Gender Based Violence"), ("Substance Abuse", "Substance Abuse")
    )

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    location = models.CharField(max_length=50, choices=LOCATIONS)
    reason = models.CharField(max_length=50, choices=REASONS)
    email = models.EmailField()
    message = models.TextField()
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.email