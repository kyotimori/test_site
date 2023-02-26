from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def tag_name(self):
        return '#' + self.caption
    
    def __str__(self):
        return self.tag_name()


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    img = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default='', blank=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tag = models.ManyToManyField(Tag)