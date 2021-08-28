from django.shortcuts import render , redirect,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from student.models import Student
from users.models import NewUser
#from users.settings import AUTH_USER_MODEL
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method=='POST':
        email = request.POST['email']
       
        password = request.POST['password']

        email = auth.authenticate(email=email,password=password)
        if email is not None:
            auth.login(request,email)
            if email.is_staff:
                m = NewUser.objects.get(email=request.POST['email'])
                request.session['member_id']=m.email
                return redirect('/')
            else:
                #print(enroll)
                m = Student.objects.get(email=request.POST['email'])
               # print(m)
                request.session['member_id']=m.email
                return HttpResponseRedirect('/')#render(request,'stdhome.html',{'email':email})#redirect('/student/stdhome')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        mobile_no=request.POST['mobile']
        course = request.POST['course']
        branch = request.POST['branch']
        sem    = request.POST['semester']
        enrol = request.POST['enrol']
        address = request.POST['address']
        password = request.POST['password']
        image = request.FILES['myfile']
        user = NewUser.objects.create_user(user_name=enrol,password=password,first_name=first_name,email=email,is_active=True)
        user.save();
        std = Student.objects.create(firstname=first_name,lastname=last_name,mobile_no=mobile_no,course=course,branch=branch,enrol=enrol,semester=sem,address=address,email=email,image=image)
        std.save();
        messages.success(request,'usercreated')
        #return redirect('/')
        #if password1 == password2:
         #   if User.objects.filter(username=username).exists():
          #      messages.info(request,'user already exists')

           # elif User.objects.filter(email=email).exists():
            #    messages.info(request,'email_taken')

            #else:
             #   user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                              # password=password1, email=email)
                # user.save();

               # messages.success(request,'usercreated')
                #return redirect('/')
        #else:
         #   messages.info(request,"password doest'n matching")


    else:
        return render(request,'register.html')


    return render(request,'register.html')

