from django.db import models
from django.contrib.postgres.fields import ArrayField

class Author(models.Model):
    username = models.CharField(max_length=33, unique=True, default='username')
    first_name = models.CharField(max_length=88)
    last_name = models.CharField(max_length=44)
    objects = models.Manager

    def __str__(self):
        return self.username

    # change upper limit to infinity
    def save(self, *args, **kwargs):
        self.username = '{}{}{}'.format(self.first_name, self.last_name, self.pk)
        super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True, to_field='username', related_name='+')
    userId = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name='+') # id of the author
    url = models.CharField(max_length=44, default='example.com') 
    title = models.CharField(max_length=44)
    body = models.TextField()
    created = models.DateField(auto_now_add= True)
    modified = models.DateField(auto_now= True)
    tags = ArrayField(models.CharField(max_length=33, default='tags')) # list of keywords
    objects = models.manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = '/posts/{}'.format(self.pk)
        word = str(self.title)
        self.tags = word.split()
        super().save(*args, **kwargs)
