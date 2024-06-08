from django.conf import settings
import datetime
from django.db import models
from django.utils import timezone
import random
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class SportCategory(models.Model):
    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name
        
class Article(models.Model):
    article_title = models.CharField('Title of the article', max_length=200)
    article_text = CKEditor5Field('Text of the article', null=True, blank=True, config_name='extends')
    pub_date = models.DateTimeField('Publication date')
    category = models.ForeignKey(SportCategory, on_delete=models.CASCADE, null=True, default=None)
    unique_id = models.IntegerField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='article_likes', blank=True)
    saved_by = models.ManyToManyField(User, related_name='saved_articles', blank=True)
    

    def like(self, user):
        self.likes.add(user)

    def unlike(self, user):
        self.likes.remove(user)
    
    
    def __str__(self):
        return self.article_title


    def save(self, *args, **kwargs):
        if not self.pk:
            while True:
                unique_id = random.randint(100000, 999999)
                if not Article.objects.filter(unique_id=unique_id).exists():
                    self.unique_id = unique_id
                    break
        super(Article, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='article_comment', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    text = models.TextField('Text', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.article_title} - {self.created_at}"