from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=CASCADE, related_name='comments')
    Comment = models.TextField()

    def __str__(self):
        return self.Comment