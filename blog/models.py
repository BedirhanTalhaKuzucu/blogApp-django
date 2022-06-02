from pyexpat import model
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    STATUS = (
        ("Published", "Published"),
        ("Draft", "Draft"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=200, default= 'https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png' )
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices = STATUS, max_length=10, default='Draft')
    
    def __str__(self):
        return self.title

class Category(models.Model):
    STATUS = (
        ("FullStack", "FullStack"),
        ("FrontEnd", "FrontEnd"),
        ("BackEnd", "BackEnd"),
    )
    category = models.CharField(choices= STATUS, max_length=10, default= 'BackEnd' )
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    def __str__(self):
        return f"[ {self.category} ] POST TITLE=> {self.post.title} " 

class Like(models.Model):
    Post = models.ForeignKey( Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"[ {self.User} ] POST TITLE=> {self.Post.title} " 


class Comment(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

class PostView(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"[ {self.timeStamp} ] POST TITLE=> {self.post.title} " 






