from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Categories table
class Category(models.Model):
    categoryName = models.CharField(max_length=200)
    subscribe = models.ManyToManyField(User)
    def __str__(self):
        return self.categoryName

class Tags(models.Model):
    tag =models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    post_image = models.ImageField(upload_to='images/',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True) 
    tags = models.ManyToManyField(Tags)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
#    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    category_name = models.ForeignKey(Category,on_delete= models.CASCADE) 
    updated_on = models.DateTimeField(auto_now= True)       
    #  slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:200]+"....."

#Comments table
class Comments(models.Model):
    user_id=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete= models.CASCADE)
    content=models.TextField()
    reply=models.ForeignKey('Comments',null=True,related_name='replies',on_delete= models.CASCADE)
    commentTime= models.DateTimeField(auto_now_add=True) 
    updated_on = models.DateTimeField(auto_now= True) 

    def removeWords(self):
        words = Word.objects.all()

        for word in words:
            self.content = self.content.replace(word.name, '*' * len(word.name))

        return self.content

    def __str__(self):
        return self.comment_body

class Likes(models.Model):
    like=models.BooleanField()
    userId=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete= models.CASCADE)

# Words list table
class Word(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

