from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'blogpapp'
urlpatterns=[
    path('', views.post_list, name='post_list'),
    
    path('<int:years>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail')

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)