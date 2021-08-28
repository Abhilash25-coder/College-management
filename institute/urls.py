from django.urls import path ,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='institute'

urlpatterns=[
path('inshome',views.inshome,name='inshome'),
path('register',views.register,name='register'),
path('managestd',views.managestd,name='managestd'),
path('deletedata/<str:enrol>/',views.delete_data,name="deletedata"),
path('staffpanel',views.staffpanel,name="staffpanel"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)