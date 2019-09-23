from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return HttpResponse('course..index...')

def get_difficulty(request):
    '''
    获取难度列表
    :param request:
    :return:  id name 【Json字符串】
    '''
    pass



def get_direction(request):
    '''
    获取方向列表
    :param request:
    :return:  id  name 【Json字符串】
    '''
    pass


# 获取 Classify【这是实例。。。】
def get_classify(request):
    '''
    获取分类列表
    :param request: direction_id // direction_name（两者为空则全部查询）
    :return: id   name  direction__name
    '''
    direction_id = None # 11
    direction_name = '' # '后端'
    if direction_id:
        res = Classify.objects.filter(direction__id=direction_id)
    else:
        res = Classify.objects.filter(direction__name__icontains=direction_name)
    res_list = list(res.values('id','name','direction__name'))
    return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)


def get_course(request):
    '''
    获取课程列表
    :param request: difficulty_name  direction_name  classify_name  page_index  page_items  sort_flag( 为0：按时间逆序，为1：选课人数，为2：收藏人数)
    :return:  id  name  introduce   course_icon   integral   publish_time【Json字符串】
    '''
    pass


def get_course_number(request):
    '''
    获取课程列表个数
    :param request: difficulty_name  direction_name  classify_name
    :return:  course_num 【Json字符串】
    '''
    pass



def search_course(request):
    '''
    获取课程列表（搜索模糊匹配）
    :param request: search_text（即 course_name 去匹配） sort_flag( 为0：按时间逆序，为1：选课人数，为2：收藏人数)】
    :return: id  name  introduce   course_icon   integral   publish_time【Json字符串】
    '''
    pass



def search_course_number(request):
    '''
    获取课程列表个数
    :param request: search_text（即 course_name 去匹配）
    :return:   course_num 【Json字符串】
    '''
    pass


def get_course_info(request):
    '''
    获取课程详细信息
    :param request: course_id
    :return:  publish_time  difficulty_name 【Json字符串】
    '''
    pass


def get_course_time(request):
    '''
    获取课程总时长（单独一个，不直接和get_video_info（）之类的函数交互）
    :param request:  course_id
    :return: course_timr【Json字符串】
    '''
    pass



def get_course_precourse(request):
    '''
    获取课程的前导课程
    :param request: course_id
    :return: id  name  difficulty__name  integral 【Json字符串】
    '''
    pass




def get_video_chapter(request):
    '''
    获取视频章节详细信息（包括哪些章哪些节） ** 调用 get_chapter() 和 get_video() **
    :param request: course_id
    :return: 【Json字符串】。。。。这一部分还不确定，，
    '''
    pass



def get_courseware_chapter(request):
    '''
    获取课件章节详细信息（包括哪些章哪些节）  ** 调用 get_chapter() 和 get_courseware() **
    :param request: course_id
    :return: 【Json字符串】。。。。这一部分还不确定，，
    '''
    pass


def get_chapter(request):
    '''
    获取课程章信息
    :param request: course_id
    :return: id  name  introduce【Json字符串】
    '''
    pass




def get_video(request):
    '''
    获取视频列表
    :param request: chapter_id
    :return: id name video_time【Json字符串】
    '''
    pass



def get_courseware(request):
    '''
    获取课件列表
    :param request:  chapter_id
    :return: id name courseware_time 【Json字符串】
    '''
    pass




def get_video_info(request):
    '''
    获取视频信息
    :param request: video_id
    :return: id  name  video_src  video_time  chapter_id 【Json字符串】
    '''
    pass



def get_courseware_info(request):
    '''
    获取章节信息
    :param request: courseware_id
    :return: id name content  courseware_time chapter_id【Json字符串】
    '''
    pass


