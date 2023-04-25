from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_CHOICES = (
    ('Dj', 'Django',),
    ('R', 'Ruby',),
)

class Post(models.Model):
    title = models.CharField( max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    custom_id = models.IntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    comment = models.ManyToManyField('Comment')
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    title = models.TextField()

