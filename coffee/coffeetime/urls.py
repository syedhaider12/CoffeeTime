from django.urls import path
from.import views


urlpatterns = [
     path('',views.home, name='main'),
     path('Coffee',views.coffe, name='coffe'),
     path('Tea',views.ta, name='tea'),
     path('Juice',views.juic, name='juice'),
     path('SignIn',views.signin, name='signin'),
     path('Contactus',views.cont, name='contact'),
     path('AboutUs',views.aboutus, name='about'),
     path('Signup',views.signup, name='signup'),
     path('logout',views.logt, name='log'),
     path('view<int:myid>/<int:subid>', views.quick, name='views')
]
