from django.db import models
from django.contrib.auth.models import User
from .models import MenuItem

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rating =  models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} review for {self.menu_item.name}:{self.rating}