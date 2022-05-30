from django.db import models
from django.urls import reverse
from cms.models.fields import PlaceholderField

# Create your models here.


class Article(models.Model):

    title = models.CharField(blank=False,max_length=256,help_text='Provide a title with maximum of 256 letters')
    slug = models.SlugField(blank=False,max_length=256,unique=True,help_text='Please enter a unique slug')
    #text = models.TextField(blank=True,help_text='Provide for the article')
    text = PlaceholderField('article_text')

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def absolute_url(self):
        return reverse('blog_app:article_detail',kwargs={'slug':self.slug})