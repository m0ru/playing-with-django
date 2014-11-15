from django.db import models

class Address(models.Model):

    street = models.CharField(max_length=200)
    houseNr = models.IntegerField()
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80)

    def __str__(self):
        return self.street + " " + str(self.houseNr) \
            + ", " + self.city + ", " + self.country


class Restaurant(models.Model):

    name = models.CharField(max_length=70)
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.name + " @ " + str(self.address)

