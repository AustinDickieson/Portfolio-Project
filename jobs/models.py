from django.db import models
#models library imported
# Create your models here

class Job(models.Model): #creates class that allows object saved inside db
    image = models.ImageField(upload_to='images/') #found in documentation, job photo
    #uploads all images to images folder
    summary = models.CharField(max_length=300) #job description

#migrations update databases to include new models
