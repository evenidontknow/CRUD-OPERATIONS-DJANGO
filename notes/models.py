from django.db import models
from django.contrib.auth.models import User         #here
 
class Notes(models.Model):
   name = models.CharField(max_length=30)
   user = models.ForeignKey(User, default=1,
                       on_delete= models.CASCADE)  #here
   def __str__(self):
       return str(self.id)+": "+self.name
   class Meta:                                     # here
       unique_together = ('user','name')
class Items(models.Model): 
    item_name = models.CharField(max_length=30, unique=True) 
    note_id = models.ForeignKey(Notes, on_delete = models.CASCADE, related_name='items')
    def __str__(self):
        return str(self.id)+": "+self.item_name


