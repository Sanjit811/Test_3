
from django.urls import path

from .views import home,signin,signup,contact,signout,enroll, attendance,profile,review

urlpatterns = [
    path('', home, name='home_rout'),
    path('signin/', signin, name='signin_rout'),
    path('signup/',signup, name='signup_rout'),
    path('contact/',contact , name='contact_rout'),
    path('signout/',signout, name='signout_rout'),
    path('enroll/',enroll,name='enroll_rout'),
    path('profile/', profile, name='profile_rout'),
    path('Attendance/', attendance, name='attendence_rout'),
    path('Review/', review, name='review_rout'),
    
]



