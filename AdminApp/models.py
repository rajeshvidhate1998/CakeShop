from django.db import models


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=20)
    def __str__(self):
        return self.cname
    class Meta:
        db_table = "Category"


class Cake(models.Model):
    cakename = models.CharField(max_length=20)
    price = models.FloatField(default=300)
    description = models.CharField(max_length=200)
    imageUrl = models.ImageField(upload_to = 'Images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "Cake"


