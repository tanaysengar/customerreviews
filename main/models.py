from django.db import models

class LookupSites(models.Model):
    sitename = models.CharField(max_length=100)

    def __str__(self):
        return self.sitename

class UPC(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code

class CustomerReviews(models.Model):
    review = models.CharField(max_length=2000)
    upc = models.ForeignKey(UPC)
    lookupsite=models.ForeignKey(LookupSites)

    def __str__(self):
        return self.review