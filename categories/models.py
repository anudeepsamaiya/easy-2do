from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL,
            related_name='sub_categories', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SubCategory'
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
