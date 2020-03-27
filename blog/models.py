from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField() #documentation
    body = models.TextField()
    image = models.ImageField(upload_to='images/')




#How to fully create blog app:
#1)Create blog model (title,publication date, body, image)
#2)Add Blog app to settings (apps.py for name), dont forget comma
#3)Create a migration (python manage.py makemigrations)
#4)Migrate (python manage.py migrate)
#5)Add to admin (jobs admin page, import class and register)
