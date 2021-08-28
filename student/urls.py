from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'student'
urlpatterns=[
    path('stdhome',views.stdhome,name='stdhome'),
    #path('logout',views.logout,name='logout'),
    #path('institutelogin',views.institutelogin,name='institutelogin'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)