from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField() #documentation
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title #makes admin title the title of the blog

    def summary(self):
        return self.body[:100] #returns first 100 characters of the body

    def pub_date_clean(self):
        return self.pub_date.strftime('%d %B %Y') #python strftime reference website




#How to fully create blog app:
#1)Create blog model (title,publication date, body, image)
#2)Add Blog app to settings (apps.py for name), dont forget comma
#3)Create a migration (python manage.py makemigrations)
#4)Migrate (python manage.py migrate)
#5)Add to admin (jobs admin page, import class and register)
