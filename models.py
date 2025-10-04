from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_percentage = models.FloatField(default=0)

    def get_final_price(self):
        """
        Return the final price after applying discount.
        """
        discount = (self.price * self.discount_percentage)/100
        return round(self.price-discount,2)
        