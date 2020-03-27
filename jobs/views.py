from django.shortcuts import render

#need to access jobs from db and display
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects #now turned into Python objects that can be used
    return render(request, 'jobs/home.html',{'jobs':jobs})#in jobs directory within templates
    #have a separate job folder within templates to decern which home.html
