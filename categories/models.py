from django.db import models
from datetime import datetime
from moderators.models import Moderator
class Category(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category_date = models.DateTimeField(default=datetime.now)
    moderator = models.ForeignKey(Moderator, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title