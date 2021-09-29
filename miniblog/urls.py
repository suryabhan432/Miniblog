from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('admin/', admin.site.urls),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('dashboard/',views.Dashboard,name='dash'),
    path('signup/',views.Signup,name='sign'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.User_logout,name='logout'),
    path('edit/<int:my_id>/',views.Edit_profile,name='edit'),
    path('delete/<int:my_id>/',views.Delete_profile,name='delete'),
]
