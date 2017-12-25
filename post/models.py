import uuid as uuid_lib

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name} ({self.uuid})'


def get_del_category():
    return Category.objects.get_or_create(name='deleted')[0]


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET(get_del_category))
    title = models.CharField(max_length=100)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title[:30]} (created: {self.created})'
