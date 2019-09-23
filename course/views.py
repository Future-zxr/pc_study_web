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
    :param request:(全部)
    :return:  id name 【Json字符串】
    '''
    difficulty = Difficulty.objects.all()
    if difficulty:
        res_list = list(difficulty.values('id', 'name'))
        return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        return JsonResponse({"Error": "获取数据错误"}, json_dumps_params={'ensure_ascii': False}, safe=False)



def get_direction(request):
    '''
    获取方向列表
    :param request:(全部)
    :return:  id  name 【Json字符串】
    '''
    direction = Direction.objects.all()
    if direction:
        res_list = list(direction.values('id', 'name'))
        return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        return JsonResponse({"Error":"获取数据错误"}, json_dumps_params={'ensure_ascii': False}, safe=False)


# 获取 Classify【这是实例。。。】
def get_classify(request):
    '''
    获取分类列表
    :param request: direction_id // direction_name（两者为空则全部查询）
    :return: id   name  direction__name
    '''
    # direction_id = None # 11
    # direction_name = '' # '后端'
    direction_id = request.GET.get('direction_id')
    direction_name = request.GET.get('direction_name')
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
    difficulty_name = request.GET.get('difficulty_name')
    direction_name = request.GET.get('direction_name')
    classify_name = request.GET.get('classify_name')
    # page_index = request.GET.get('page_index')
    # sort_flag = request.GET.get('sort_flag')
    page_items = 5
    page_index = 1

    sort_flag = 1

    if sort_flag == 0:
        data = Course.objects.filter(difficulty__name__icontains=difficulty_name,classify__direction__name__icontains=direction_name,
                                     classify__name__icontains=classify_name).order_by('-publish_time')[:5]
    elif sort_flag == 1:
        from django.db.models import Count
        from user_course.models import SelectCourse
        # users = SelectCourse.objects.values('course__name').annotate(select_num = Count('course_id')).order_by('-select_num')
        # print(users.values())
        # result = users.values('course__id','course__name','course__introduce',
        #                    'course__course_icon','course__integral','course__publish_time')
        # for res in result:
        #     res['course__publish_time']=res['course__publish_time'].strftime('%Y-%m-%d %H:%M:%S')
        # return JsonResponse(list(result), json_dumps_params={'ensure_ascii': False}, safe=False)
    # return HttpResponse('ok')
    result = data.values('id','name','introduce','course_icon','integral','publish_time')
    for res in result:
        res['publish_time']=res['publish_time'].strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse(list(result), json_dumps_params={'ensure_ascii': False}, safe=False)





def get_course_number(request):
    '''
    获取课程列表个数
    :param request: difficulty_name  direction_name  classify_name
    :return:  course_num 【Json字符串】
    '''
    difficulty_name = request.GET.get('difficulty_name')
    direction_name = request.GET.get('direction_name')
    classify_name = request.GET.get('classify_name')

    data = Course.objects.filter(difficulty__name__icontains=difficulty_name,classify__direction__name__icontains=direction_name,
                                 classify__name__icontains=classify_name).count()
    return JsonResponse({"course_num": data}, json_dumps_params={'ensure_ascii': False}, safe=False)



def search_course(request):
    '''
    获取课程列表（搜索模糊匹配）
    :param request: search_text（即 course_name 去匹配） sort_flag( 为0：按时间逆序，为1：选课人数，为2：收藏人数)】
    :return: id  name  introduce   course_icon   integral   publish_time【Json字符串】
    '''
    search_text = request.GET.get('search_text')
    # sort_flag = request.GET.get('sort_flag')
    sort_flag = 0

    if search_text:
        if sort_flag == 0:
            data = Course.objects.filter(name__icontains=search_text).order_by('-publish_time')
            result = list(data.values('id','name','introduce','course_icon','integral','publish_time'))
            for res in result:
                res['publish_time']=res['publish_time'].strftime('%Y-%m-%d %H:%M:%S')
            return JsonResponse(result, json_dumps_params={'ensure_ascii': False}, safe=False)
        elif sort_flag == 1:
            pass
        else:
            pass
    else:
        return JsonResponse({"Error": "请输入搜素关键词"}, json_dumps_params={'ensure_ascii': False}, safe=False)





def search_course_number(request):
    '''
    获取课程列表个数
    :param request: search_text（即 course_name 去匹配）
    :return:   course_num 【Json字符串】
    '''
    search_text = request.GET.get('search_text')
    if search_text:
        data = Course.objects.filter(name__icontains=search_text).count()
        return JsonResponse({"course_num": data}, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        return JsonResponse({"Error": "请输入搜素关键词"}, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_course_info(request):
    '''
    获取课程详细信息
    :param request: course_id
    :return: name  introduce   course_icon  notice  integral
    difficulty_name  direction_name  classify_name study_people collection_people
    '''
    from django.db.models import Count
    from user_course.models import SelectCourse, Collection
    id = request.GET.get('course_id')

    course_data = Course.objects.filter(id=id)
    # 课程名，介绍，课程图片，课程须知，
    result = list(course_data.values('name', 'introduce', 'course_icon', 'notice', 'integral', 'difficulty__name', 'classify__name', 'classify__direction__name'))
    # 选课人数的判断
    select_data = SelectCourse.objects.filter(course_id=id).values('course_id')\
        .annotate(study_people=Count('course_id'))
    if select_data:
        select_res = list(select_data.values('study_people'))[0]['study_people']
    else:
        select_res = 0
    result[0]['study_people'] = select_res

    # 课程是否被收藏
    collection_data = Collection.objects.filter(course_id=id).values('course_id')\
        .annotate(collection_people=Count('course_id'))
    if collection_data:
        collection_res = list(collection_data.values('collection_people'))[0]['collection_people']
    else:
        collection_res = 0
    result[0]['collection_people'] = collection_res
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_course_time(request):
    '''
    获取课程总时长（单独一个，不直接和get_video_info（）之类的函数交互）
    :param request:  course_id
    :return: course_time【Json字符串】
    '''
    from utils import time_to_stamp,stamp_to_time
    time_stamp= 0
    course_id = request.GET.get('course_id')

    courseware_data = Courseware.objects.filter(chapter__course_id=course_id)
    courseware_time = list(courseware_data.values('courseware_time'))
    video_data = Video.objects.filter(chapter__course_id=course_id)
    video_time = list(video_data.values('video_time'))

    for i in range(len(courseware_time)):
        courseware_time[i]['courseware_time']= time_to_stamp(courseware_time[i]['courseware_time'])
        time_stamp += courseware_time[i]['courseware_time']

    for i in range(len(video_time)):
        video_time[i]['video_time'] = time_to_stamp(video_time[i]['video_time'])
        time_stamp += video_time[i]['video_time']

    course_time = stamp_to_time(time_stamp)
    return JsonResponse({"course_time":course_time}, json_dumps_params={'ensure_ascii': False}, safe=False)




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
    course_id = request.GET.get('course_id')
    course_video = Video.objects.filter(chapter__course_id=course_id)
    res_list = list(course_video.values('id','name','chapter_id'))
    chapter_info = get_chapter(request)
    for i in range(len(chapter_info)):
        chapter_info[i]['video'] = None
        for j in range(len(res_list)):
            if chapter_info[i]['id'] == res_list[j]['chapter_id']:
                if chapter_info[i]['video']:
                    chapter_info[i]['video'].append({"video_name": res_list[j]['name'], "video_id": res_list[j]['id']})
                else:
                    chapter_info[i]['video'] = [{"video_name": res_list[j]['name'], "video_id": res_list[j]['id']}]
                # res_list.remove(res_list[j])
    return JsonResponse(chapter_info, json_dumps_params={'ensure_ascii': False}, safe=False)



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
    course_id = request.GET.get('course_id')
    chapter_data = Chapter.objects.filter(course_id=course_id)
    res_list = list(chapter_data.values('id','name','introduce'))
    return res_list
    # return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)





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


