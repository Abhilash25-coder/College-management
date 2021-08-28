from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from django.contrib.auth.models import User , auth,NewUser
from django.contrib.auth import get_user_model
from .models import Faculty
from users.models import NewUser
from student.models import Student
# Create your views here.
def inshome(request):
    return render(request,'inshome.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        mobile_no=request.POST['mobile']
        course = request.POST['course']
        branch = request.POST['branch']        
        enrol = request.POST['enrol']
        address = request.POST['address']
        password = request.POST['password']
        image = request.FILES['myfile']
        user = NewUser.objects.create_user(user_name=enrol,password=password,first_name=first_name,email=email,is_active=True,is_staff=True)
        user.save();
        ft = Faculty.objects.create(firstname=first_name,lastname=last_name,mobile_no=mobile_no,course=course,branch=branch,enroll=enrol,address=address,email=email,image=image)
        ft.save();
        messages.success(request,'usercreated')
    else:
        pass

    return render(request,'registerfaculty.html')


def managestd(request):

    students=Student.objects.get_queryset
    return render(request,'managestd.html',{'students':students})

def delete_data(request,enrol):
    if request.method == 'POST':
        user_name=enrol
        pi = NewUser.objects.get(user_name=enrol)
        st= Student.objects.get(enrol=enrol)
        st.delete()
        pi.delete()
        return redirect('/')

def staffpanel(request):
     stf_id = request.session['member_id']
   # print(std_id)
     Facultys=Faculty.objects.get(email=stf_id)
    #print(Std)
     return render(request,'staffpanel.html',{'stf_id':stf_id ,'Facultys':Facultys})