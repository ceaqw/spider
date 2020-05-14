from django.db import models

# Create your models here.


class MyBook(models.Model):
    """图书类"""
    title_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)

    class Meta:
        db_table = "book"
