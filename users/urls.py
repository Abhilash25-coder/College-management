from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'users'
urlpatterns=[
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
   path('register',views.register,name='register'),
   #path('delete_data/<int:email>/',views.delete_data,name="delete_data")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
