from django.db import models

# Create your models here.
class Reciṕe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    prepartion_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)

    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)

    preparation_steps = models.TextFiels()

    preparation_steps_is_html = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/')

    
