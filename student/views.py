from django.shortcuts import render , redirect
from users.models import NewUser
from .models import Student
from django.contrib.sessions.models import Session
# Create your views here.
def stdhome(request):
   # s = Session.objects.all()
   # s.get_decoded()
   
    std_id = request.session['member_id']
   # print(std_id)
    Students=Student.objects.get(email=std_id)
    #print(Std)
    return render(request,'stdhome.html',{'std_id':std_id,'Students':Students})
    #return render(request,'stdhome.html')