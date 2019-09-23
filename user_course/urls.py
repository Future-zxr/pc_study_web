from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^is_collection/',views.is_collection,name='is_collection'),
    url('^collection_course/',views.collection_course,name='collection_course'),
    url('^delete_collection_course/',views.delete_collection_course,name='delete_collection_course'),
    url('^get_collection_number/',views.get_collection_number,name='get_collection_number'),
    url('^get_collection_peruser/',views.get_collection_peruser,name='get_collection_peruser'),
    url('^get_collection_number_peruser/',views.get_collection_number_peruser,name='get_collection_number_peruser'),
    url('^is_sc/',views.is_sc,name='is_sc'),
    url('^insert_sc/',views.insert_sc,name='insert_sc'),
    url('^update_sc/',views.update_sc,name='update_sc'),
    url('^get_sc_number/',views.get_sc_number,name='get_sc_number'),
    url('^get_sc_peruser/',views.get_sc_peruser,name='get_sc_peruser'),
    url('^get_sc_number_peruser/',views.get_sc_number_peruser,name='get_sc_number_peruser'),
    url('^study_progress/',views.study_progress,name='study_progress'),
    url('^insert_course_eva/',views.insert_course_eva,name='insert_course_eva'),
    url('^get_course_eva/',views.get_course_eva,name='get_course_eva'),
    url('^insert_user_video/',views.insert_user_video,name='insert_user_video'),
    url('^update_user_video/',views.update_user_video,name='update_user_video'),
    url('^get_user_video/',views.get_user_video,name='get_user_video'),
    url('^insert_question_video/',views.insert_question_video,name='insert_question_video'),
    url('^get_question_video/',views.get_question_video,name='get_question_video'),
    url('^insert_user_courseware/',views.insert_user_courseware,name='insert_user_courseware'),
    url('^get_user_courseware/',views.get_user_courseware,name='get_user_courseware'),
    url('^insert_question_courseware/',views.insert_question_courseware,name='insert_question_courseware'),
    url('^get_question_courseware/',views.get_question_courseware,name='get_question_courseware'),
]