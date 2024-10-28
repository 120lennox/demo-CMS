from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_field=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    name = models.CharField(max_length=100)
    page = models.ForeignKey(Page, related_name='sections', on_delete=models.CASCADE)
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        order = ['order']

    def __str__(self):
        return f'{self.page.title} - {self.name}'
