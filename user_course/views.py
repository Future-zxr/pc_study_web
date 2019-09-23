from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('user_course...index...')



def is_collection(request):
    '''
    判断是否收藏
    :param request:  user_id  course_id
    :return: 是否
    '''
    pass

def collection_course(request):
    '''
    收藏课程
    :param request: user_id course_id
    :return:
    '''
    pass

def delete_collection_course(request):
    '''
    取消收藏
    :param request:
    :return:
    '''
    pass

def get_collection_number(request):
    '''
    获取收藏人数
    :param request:  course_id
    :return:  collection_num 【Json字符串】
    '''
    pass

def get_collection_peruser(request):
    '''
    查询用户收藏的所有课程
    :param request: user_id
    :return: id name integral publish_time【Json字符串】
    '''
    pass

def get_collection_number_peruser(request):
    '''
    查询用户收藏的所有课程的个数
    :param request: user_id
    :return: course_num【Json字符串】
    '''
    pass

def is_sc(request):
    '''
    判断用户是否选课
    :param request: user_id course_id
    :return:
    '''
    pass

def insert_sc(request):
    '''
    添加用户选课
    :param request: user_id course_id
    :return:
    '''
    pass

def update_sc(request):
    '''
    修改用户选课
    :param request:
    :return:
    '''
    pass

def get_sc_number(request):
    '''
    查询选课人数
    :param request:  course_id
    :return: user_num【Json字符串】
    '''
    pass

def get_sc_peruser(request):
    '''
    查询某用户选择的所有课程
    :param request:  user_id iscomplete？
    :return:  id name integral publish_time【Json字符串】
    '''
    pass


def get_sc_number_peruser(request):
    '''
    查询某用户选择的所有课程个数
    :param request:  user_id
    :return:  course_num【Json字符串】
    '''
    pass

def study_progress(request):
    '''
    获取用户学习进度
    :param request: user_id  course_id
    :return:  stu_pro【Json字符串】
    '''
    pass

def insert_course_eva(request):
    '''
    添加用户对课程的评价
    :param request: content user_id course_id
    :return: 添加状态【Json字符串】
    '''
    pass

def get_course_eva(request):
    '''
    查询该课程的所有用户评价
    :param request: course_id
    :return: content user_info__name user_info_icon eva_date【Json字符串】
    '''
    pass

def insert_user_video(request):
    '''
    添加用户看视频的进度
    :param request:  user_id  video_id
    :return:
    '''
    pass

def update_user_video(request):
    '''
    修改用户看视频的进度
    :param request:  user_id  video_id progress
    :return:
    '''
    pass

def get_user_video(request):
    '''
    查询用户看视频的进度
    :param request:  user_id  video_id
    :return: progress【Json字符串】
    '''
    pass

def insert_question_video(request):
    '''
    添加用户对某视频的提问
    :param request: content  user_id  video_id question_video_id？
    :return:
    '''
    pass

def get_question_video(request):
    '''
    查询某视频的所有用户提问
    :param request: video_id
    :return: content user_info_icon user_info_name question_video qv_date【Json字符串】
    '''
    pass

def insert_user_courseware(request):
    '''
    添加用户课件
    :param request:  user_id  courseware_id iswatch=1
    :return:
    '''
    pass

def get_user_courseware(request):
    '''
    查询用户课件
    :param request:  user_id  courseware_id
    :return: iswatch【Json字符串】
    '''
    pass

def insert_question_courseware(request):
    '''
    添加用户对某课件的提问
    :param request: content  user_id  courseware_id question_courseware_id？
    :return:
    '''
    pass

def get_question_courseware(request):
    '''
    查询某课件的所有用户提问
    :param request: courseware_id
    :return: content user_info_icon user_info_name question_courseware qc_date【Json字符串】
    '''
    pass

