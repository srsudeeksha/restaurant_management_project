from django.db import models

class Resturant(models.Model):
    name = models.CharField(max_length=255)

    opening_days = models.CharField(
        max_length=50,
        help_text="Comma-separated days. E.g. 'Mon,Tue,Wed,Thu,Fri'"
    )
    