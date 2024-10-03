from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Contact,Membership,Trainer,Enrollment, Attendance





# Create your views here.

def home(request):
    return render(request, 'Utkal_Gym_app/index.html')


 # create Login Sighin modal

def signin(request):
    if request.method == 'POST':
        user_Number = request.POST.get('signinPhoneNumber')
        user_Password = request.POST.get('signinPassword')
        #print(user_Number,user_Password)


        obj_User = None

        try:
            obj_User = authenticate(request, username=user_Number, password=user_Password)
            #print(obj_User)

        except:
            messages.error(request, 'Invalid Credentria')

        if obj_User is not None:
            login(request,obj_User)
            messages.success(request, 'Loggedin Sucessfully')
            return redirect('home_rout')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home_rout')
    return redirect(request, 'Utkal_Gym_app/LoginModal.html')


# create signup 

def signup(request):
    if request.method == 'POST':
        user_Number = request.POST.get('userNumber')
        user_Email = request.POST.get('userEmail')
        user_Password = request.POST.get('userPassword')
        user_confPassword = request.POST.get('confPassword')
        # print(user_Number, user_Email, user_Password, user_confPassword )

        if user_Password != user_confPassword:
            messages.info(request, "Password not matching")
            #print(user_Password, user_confPassword )
            return redirect('signup_rout')
        
        if len(user_Number) != 10:
            #messages.info(request, "Incorrect Phone Number")
            messages.success(request, "Incorrect Phone Number")
            return redirect("signup_rout")
        
        try:
            if User.objects.get(username=user_Number):  
                messages.warning(request, " phone number is already taken")
                
                return redirect('signup_rout')
            
            # existing_user = User.objects.get(username=user_Number)
            # if existing_user==user_Number:
            #     messages.error(request, "Phone number is already taken")
            #     return redirect('signup_rout')
        except Exception as identifire:
            pass

        try:
            if User.objects.get(email=user_Email):
                messages.warning(request, "Email is already taken")
                return redirect('signup_rout')
        except Exception as identifire:
            pass

        user = User.objects.create_user(username=user_Number, email=user_Email, password=user_Password)
        user.save()

        if (user.is_active):
            messages.success(request, "User registration successful, Plz signin")
            return redirect('home_rout')
        else:
            messages.warning(request, "user already Registered.")

    return render(request, 'Utkal_Gym_app/signupModal.html')


# contact page

def contact(request):
    if request.method == 'POST':
        cnt_Name = request.POST.get('cntName')
        cnt_Email = request.POST.get('cntEmail')
        cnt_Number = request.POST.get('cntNumber')
        cnt_Description = request.POST.get('cntDescription')
        
        #print(cnt_Name, cnt_Email, cnt_Number, cnt_Description)

        obj_Contact = Contact()
        obj_Contact.Name = cnt_Name 
        obj_Contact.E_mail = cnt_Email
        obj_Contact.Phone_Number = cnt_Number
        obj_Contact.Description = cnt_Description


        obj_Contact.save()
        messages.info(request, 'Thanks for Contacting us we will get back to you soon')
        

    return render(request, 'Utkal_Gym_app/contact.html')


# signout create
def signout(request):
    logout(request)
    messages.success(request, 'logged Out successfully')
    return redirect('home_rout')


 # enroll create

def enroll(request):
     if request.user.is_authenticated:
        #obj_Membership_Plan = Membership_Plan.objects.all()
        obj_Membership_Plan = Membership.objects.all()
        #print('obj_Membership_Plan')

        obj_Trainer = Trainer.objects.values_list('Trainer_Name', flat=True).order_by('-Trainer_ID')

        data = {
            'membership': obj_Membership_Plan,
            'trainer': obj_Trainer,
        }
        if request.method == 'POST':
            enrl_Name = request.POST.get('enrName')
            enrl_Email = request.POST.get('enrEmail')
            enrl_Gender = request.POST.get('ernGender')
            enrl_PhoneNumber = request.POST.get('enrNumber')
            enrl_DateOfBirth = request.POST.get('enrDob')
            enrl_Plan = request.POST.get('enr_membership_plane')
            enrl_Trainer = request.POST.get('enr_Trainer')
            enrl_Reference = request.POST.get('enrReference')
            enrl_Address = request.POST.get('enrAddress')




           # print(enrl_Name, enrl_Email, enrl_Gender, enrl_PhoneNumber, enrl_DateOfBirth, enrl_Plan, enrl_Trainer, enrl_Reference, enrl_Address)


            obj_Enroll = Enrollment()
            obj_Enroll.Enrollment_Full_Name = enrl_Name
            obj_Enroll.Enrollment_Email = enrl_Email
            obj_Enroll.Enrollment_Gender = enrl_Gender
            obj_Enroll.Enrollment_Number = enrl_PhoneNumber
            obj_Enroll.Enrollment_DOB = enrl_DateOfBirth
            obj_Enroll.Enrollment_Selecte_membership_plan = enrl_Plan
            obj_Enroll.Enrollment_Selected_Trainer = enrl_Trainer
            obj_Enroll.Enrollment_Reference = enrl_Reference
            obj_Enroll.Enrollment_Address = enrl_Address
            obj_Enroll.is_Active = True

            obj_Enroll.save()
            messages.success(request, 'Thanks for Enrollment.')
            return redirect('enroll_rout')
        else:
            return render(request, 'Utkal_Gym_app/enroll.html', context=data)
     else:
         
        messages.warning(request, 'Please Login and Try Again.')
        return redirect('home_rout')




# # # profile create

def profile(request):
    if request.user.is_authenticated:
        user_name = request.user
        obj_Enroll = Enrollment.objects.filter(Enrollment_Number = user_name)
        obj_Attendance = Attendance.objects.filter(phone_Number= user_name)

        data = {
            'profile_details':obj_Enroll ,
            'attendance_details': obj_Attendance
            }
        return render(request,'Utkal_Gym_app/viewProfile.html', context=data)
    else:
        messages.warning(request, 'please login and try again')
        return redirect('home_rout')


# # # create attendance 

def attendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            phoneNumber = request.POST.get('attndNumber')
            Login_time = request.POST.get('attndLoginTime')
            logout_time = request.POST.get('attndLogoutTime')
            workout= request.POST.get('attndWorkout')
            trainer = request.POST.get('attndTrainer')
            # print("logIn Time is {0}, logOut Time is {1}".format(Login_time,logout_time))

            obj_attendance = Attendance()
            obj_attendance.phone_Number = phoneNumber
            obj_attendance.log_in = Login_time
            obj_attendance.log_out = logout_time
            obj_attendance.Selected_workout = workout
            obj_attendance.trained_By = trainer

            obj_attendance.save()
            messages.success(request, 'Attendance applied successfully')
            return redirect('home_rout')
        
        selectTrainer = Trainer.objects.all()

        data = {
            'trainer_details': selectTrainer
        }
        return render(request, 'Utkal_Gym_app/Attendence.html' , context=data )

    else:
        messages.warning(request, 'plz login and try again')
        return redirect('home_rout')
    


# create customber feedback form here


def review(request):
    return render(request, 'Utkal_Gym_app/Review.html')
