from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=[str(self.id),])



class Comment(models.Model):
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    article = models.ForeignKey(Article,related_name= 'comments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.writer)+"  "+str(self.id)


    def get_absolute_url(self):
        return reverse('article_list')