from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null= False,blank = True,unique=True,db_index=True, editable= False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,*kwargs)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null= False,blank = True,unique=True,db_index=True, editable= False)
    type = models.ForeignKey(Type,null=True, on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,*kwargs)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null= False,blank = True,unique=True,db_index=True, editable= False)
    category = models.ForeignKey(Category,null= True, on_delete=models.CASCADE)
    type = models.ForeignKey(Type,null= True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,*kwargs)

