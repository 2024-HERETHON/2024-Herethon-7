from django.conf import settings
from django.conf.urls.static import static

# homeapp/urls.py
app_name='homeapp'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exercise-info/', views.exercise_info_list, name='exercise_info_list'),
    path('exercise-info/<int:pk>/', views.exercise_info_detail, name='exercise_info_detail'),
    path('walking-course/', views.walking_course_list, name='walking_course_list'),
    path('walking-course/<int:pk>/', views.walking_course_detail, name='walking_course_detail'),
    path('splash1',views.splash1,name='splash'),
    path('splash2',views.splash2,name='splash'),
    path('splash3',views.splash3,name='splash'),
    path('splash4',views.splash4,name='splash'),
    path('splash5',views.splash5,name='splash'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
