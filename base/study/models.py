from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#this is topic models
class Topic(models.Model):
          name=models.CharField(max_length=200)
          def __str__(self):
              return self.name
#end topic
class Room(models.Model):
          user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
          
          topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
          name=models.CharField(max_length=200)
          description=models.TextField(null=True,blank=True)
          update=models.DateTimeField(auto_now=True)
          created=models.DateTimeField(auto_now_add=True) 
          
          def __str__(self):
              return self.name
# this is messages medels
class Messages(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE)
          room=models.ForeignKey(Room,on_delete=models.CASCADE)
          body=models.TextField()
          update=models.DateTimeField(auto_now=True)
          created=models.DateTimeField(auto_now_add=True)
          def __str__(self):
              return self.body [0:50]
          
          
#end messages models

          
          
