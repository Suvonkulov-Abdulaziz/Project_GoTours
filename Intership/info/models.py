from django.db import models

# Create your models here.
class Tickets(models.Model):
    image = models.ImageField(upload_to="images/")
    hotel = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Ticket'

class ContactView(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

class CategoryFLightModel(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class TravelClassModel(models.Model):
    name = models.CharField(max_length=128, default = 'Economy'
    )
    def __str__(self):
        return self.name
class FlightModel(models.Model):
    flying_from = models.CharField(max_length=128)
    flying_to = models.CharField(max_length=128)
    departing = models.DateField()
    returning = models.DateField()
    number_of_adults = models.PositiveIntegerField(default=0)
    number_of_children = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(CategoryFLightModel, on_delete=models.CASCADE)
    travelClass = models.ForeignKey(TravelClassModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flying_from} - {self.flying_to}"

    class Meta:
        verbose_name = "Flights"
        verbose_name_plural = "Flights"

