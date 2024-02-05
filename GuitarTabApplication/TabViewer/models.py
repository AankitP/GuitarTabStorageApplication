from django.db import models

# Create your models here.
class GuitarTab(models.Model):
    Title = models.CharField(max_length = 100) # Song Title
    Artist = models.CharField(max_length = 100) # artist name
    Location = models.CharField(max_length = 300) # this is location in Directory
    Added_Date = models.DateTimeField("Date Added") # this is to keep track of when the tabs were added
    
