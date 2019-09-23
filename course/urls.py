from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^get_difficulty/',views.get_difficulty,name='get_difficulty'),
    url('^get_direction/',views.get_direction,name='get_direction'),
    url('^get_classify/',views.get_classify,name='get_classify'),
    url('^get_course/',views.get_course,name='get_course'),
    url('^get_course_number/',views.get_course_number,name='get_course_number'),
    url('^search_course/',views.search_course,name='search_course'),
    url('^search_course_number/',views.search_course_number,name='search_course_number'),
    url('^get_course_info/',views.get_course_info,name='get_course_info'),
    url('^get_course_time/',views.get_course_time,name='get_course_time'),
    url('^get_video_chapter/',views.get_video_chapter,name='get_video_chapter'),
    url('^get_chapter/',views.get_chapter,name='get_chapter'),
    url('^get_video/',views.get_video,name='get_video')
]