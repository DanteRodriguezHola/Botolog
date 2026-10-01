from django.db import models

class Post(models.Model):
    heading = models.CharField(max_length = 255)
    shortened_heading = models.CharField(max_length = 255)
    slug = models.SlugField()
    drophead = models.TextField()
    content = models.TextField()
    
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.date} - {self.shortened_heading}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)