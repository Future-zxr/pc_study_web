from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from user.models import User
from course.models import Course,Video,Courseware


# Create your views here.
def index(request):
    return HttpResponse('user_course...index...')



def is_collection(request):
    '''
    判断是否收藏
    :param request:  user_id  course_id
    :return: 是否
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    res = Collection.objects.filter(user__id=user_id,course__id=course_id)
    if res:
        res_list = True
    else:
        res_list = False
    res_list = json.dumps({"result":res_list})
    return HttpResponse(res_list)





def collection_course(request):
    '''
    收藏课程
    :param request: user_id course_id
    :return:
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    user_f = User.objects.filter(id = user_id).first()
    course_f = Course.objects.filter(id = course_id).first()
    res = None
    try:
        Collection.objects.create(user=user_f,course=course_f)
        res = 'collection success'
    except Exception as ex:
        print(ex)
        res = 'collection error'
    finally:
        res_json = json.dumps({"result":res})
        return HttpResponse(res_json)




def delete_collection_course(request):
    '''
    取消收藏
    :param request: user_id course_id
    :return:
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    res = None
    try:
        Collection.objects.filter(user__id = user_id,course__id = course_id).delete()
        res = 'delete success'
    except Exception as ex:
        print(ex)
        res = 'delete error'
    finally:
        res_json = json.dumps({"result":res})
        return HttpResponse(res_json)





def get_collection_number(request):
    '''
    获取收藏人数
    :param request:  course_id
    :return:  collection_num 【Json字符串】
    '''
    course_id = request.GET.get('course_id')
    print(course_id)
    col = Collection.objects.filter(course__id = course_id).count()
    res_list = json.dumps({"collection_num":col})
    return HttpResponse(res_list)





def get_collection_peruser(request):
    '''
    查询用户收藏的所有课程
    :param request: user_id
    :return: id name integral publish_time【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    courses = Collection.objects.filter(user__id = user_id).distinct().values('course__id','course__name','course__integral','course__publish_time')
    courses = list(courses)
    for i in range(len(courses)):
        courses[i]['course__publish_time'] = courses[i]['course__publish_time'].strftime('%Y-%m-%d %H:%M:%S')
    courses = json.dumps(courses)
    return HttpResponse(courses)





def get_collection_number_peruser(request):
    '''
    查询用户收藏的所有课程的个数
    :param request: user_id
    :return: course_num【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    course_num = Collection.objects.filter(user__id = user_id).distinct().count()
    course_num = json.dumps({"course_num":course_num})
    return HttpResponse(course_num)



def is_sc(request):
    '''
    判断用户是否选课
    :param request: user_id course_id
    :return:
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    sc = SelectCourse.objects.filter(user__id = user_id, course__id = course_id).count()
    if sc:
        res = True
    else:
        res = False
    res_list = json.dumps({"result":res})
    return HttpResponse(res_list)



def insert_sc(request):
    '''
    添加用户选课
    :param request: user_id course_id
    :return:
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    user_f = User.objects.filter(id = user_id).first()
    course_f = Course.objects.filter(id = course_id).first()
    res = None
    try:
        sc = SelectCourse.objects.create(user = user_f,course = course_f, iscomplete= 0)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        res_json = {"result":res}
        return HttpResponse(json.dumps(res_json))



def update_sc(request):
    '''
    修改用户选课
    :param request: user_id course_id
    :return:
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    res = None
    try:
        sc = SelectCourse.objects.filter(user__id = user_id, course__id = course_id).first()
        sc.iscomplete = 1
        sc.save()
        res = "update success"
    except Exception as ex:
        print(ex)
        res = "update error"
    finally:
        res_json = {"result":res}
        return HttpResponse(json.dumps(res_json))



def get_sc_number(request):
    '''
    查询选课人数
    :param request:  course_id
    :return: user_num【Json字符串】
    '''
    course_id = request.GET.get('course_id')
    user_num = SelectCourse.objects.filter(course__id = course_id).distinct().count()
    res_json = {"user_num":user_num}
    return HttpResponse(json.dumps(res_json))



def get_sc_peruser(request):
    '''
    查询某用户选择的课程
    :param request:  user_id iscomplete
    :return:  id name integral sc_date【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    iscomplete = request.GET.get('iscomplete')
    if iscomplete:
        courses = SelectCourse.objects.filter(user__id=user_id, iscomplete = int(iscomplete))
    else:
        courses = SelectCourse.objects.filter(user__id = user_id)
    courses_list = list(courses.values('course__id','course__name','course__integral','sc_date'))
    for i in range(len(courses_list)):
        courses_list[i]['sc_date'] = courses_list[i]['sc_date'].strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(json.dumps(courses_list))





def get_sc_number_peruser(request):
    '''
    查询某用户选择的课程个数
    :param request:  user_id iscomplete
    :return:  course_num【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    iscomplete = request.GET.get('iscomplete')
    if iscomplete:
        course_num = SelectCourse.objects.filter(user__id=user_id, iscomplete=int(iscomplete)).count()
    else:
        course_num = SelectCourse.objects.filter(user__id=user_id).count()
    courses_json = {"course_num":course_num}
    return HttpResponse(json.dumps(courses_json))





def calculate_time(obj, name):
    # obj = UserVideo.objects.filter(user__id=user_id, video__chapter__course__id=course_id).values('progress')
    from utils.time_util import time_to_stamp
    obj_list = list(obj)
    time_stamp = 0
    for i in range(len(obj_list)):
        time_stamp += time_to_stamp(obj_list[i][name])
    return time_stamp



def study_progress(request):
    '''
    获取用户学习进度
    :param request: user_id  course_id
    :return:  stu_pro（进度百分比）【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')

    user_time_stamp = 0
    # 用户视频
    videos = UserVideo.objects.filter(user__id = user_id,video__chapter__course__id=course_id).values('progress')
    if videos:
        user_time_stamp += calculate_time(videos,'progress')
   # 用户课件
    coursewares = UserCourseware.objects.filter(user__id = user_id,courseware__chapter__course__id=course_id).values('courseware__courseware_time')
    if coursewares:
        user_time_stamp += calculate_time(coursewares,'courseware__courseware_time')

    course_time_stamp = 0
    # 课程视频
    course_videos = Video.objects.filter(chapter__course__id=course_id).values('video_time')
    if course_videos:
        course_time_stamp += calculate_time(course_videos, 'video_time')

    # 课程课件
    course_coursewares = Courseware.objects.filter(chapter__course__id=course_id).values('courseware_time')
    if course_coursewares:
        course_time_stamp += calculate_time(course_coursewares, 'courseware_time')

    stu_pro = 0
    if course_time_stamp:
        stu_pro = user_time_stamp*100 // course_time_stamp
    return HttpResponse(json.dumps({"stu_pro":stu_pro}))



def insert_course_eva(request):
    '''
    添加用户对课程的评价
    :param request: content user_id course_id
    :return: 添加状态【Json字符串】
    '''
    content = request.GET.get('content')
    user_id = request.GET.get('user_id')
    course_id = request.GET.get('course_id')
    res = None
    try:
        user_f = User.objects.filter(id=user_id).first()
        course_f = Course.objects.filter(id=course_id).first()
        ce = CourseEvaluation.objects.create(content=content,user=user_f,course=course_f)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        res_json = json.dumps({"result":res})
        return HttpResponse(res_json)




def get_course_eva(request):
    '''
    查询该课程的所有用户评价
    :param request: course_id
    :return: content user__userinfo__user_name user_info_icon eva_date【Json字符串】
    '''
    course_id = request.GET.get('course_id')
    ces = CourseEvaluation.objects.filter(course__id = course_id).values('content','user__userinfo__user_name','user__userinfo__user_icon__icon_img','eva_date')
    ces_list = list(ces)
    for i in range(len(ces_list)):
        ces_list[i]['eva_date']= ces_list[i]['eva_date'].strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(json.dumps(ces_list))




def insert_user_video(request):
    '''
    添加用户看视频的进度
    :param request:  user_id  video_id
    :return:
    '''
    user_id = request.GET.get('user_id')
    video_id = request.GET.get('video_id')
    user_f = User.objects.filter(id=user_id).first()
    video_f = Video.objects.filter(id = video_id).first()
    res = None
    try:
        UserVideo.objects.create(user = user_f, video = video_f, progress='0:0:0')
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        return HttpResponse(json.dumps({"result":res}))




def update_user_video(request):
    '''
    修改用户看视频的进度
    :param request:  user_id  video_id progress（时间戳格式）
    :return:
    '''
    from utils.time_util import stamp_to_time
    user_id = request.GET.get('user_id')
    video_id = request.GET.get('video_id')
    progress = request.GET.get('progress')
    progress = stamp_to_time(progress)
    res = None
    try:
        uv = UserVideo.objects.filter(user__id = user_id,video__id=video_id).first()
        uv.progress = progress
        uv.save()
        res = 'update success'
    except Exception as ex:
        print(ex)
        res = 'update error'
    finally:
        return HttpResponse(json.dumps({"result":res}))



def get_user_video(request):
    '''
    查询用户看视频的进度
    :param request:  user_id  video_id
    :return: progress（时间戳）【Json字符串】
    '''
    from utils.time_util import time_to_stamp
    user_id = request.GET.get('user_id')
    video_id = request.GET.get('video_id')
    progress = UserVideo.objects.filter(user__id=user_id,video__id=video_id).values('progress')[0]['progress']
    progress_stamp = time_to_stamp(progress)
    return HttpResponse(json.dumps({"progress":progress_stamp}))




def insert_question_video(request):
    '''
    添加用户对某视频的提问
    :param request: content  user_id  video_id question_video_id
    :return:
    '''
    content = request.GET.get('content')
    user_id = request.GET.get('user_id')
    video_id = request.GET.get('video_id')
    question_video_id = request.GET.get('question_video_id')
    user_f = User.objects.filter(id=user_id).first()
    video_f = Video.objects.filter(id=video_id).first()
    res = None
    try:
        if question_video_id:
            question_video = QuestionVideo.objects.filter(id = question_video_id).first()
            QuestionVideo.objects.create(content=content, video=video_f,user=user_f,question_video=question_video)
        else:
            QuestionVideo.objects.create(content=content, video=video_f, user=user_f)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        return HttpResponse(json.dumps({"result": res}))



def get_question_video(request):
    '''
    查询某视频的所有用户提问
    :param request: video_id
    :return: content user_info_icon user_info_name question_video qv_date【Json字符串】
    '''
    video_id = request.GET.get('video_id')
    qvs = QuestionVideo.objects.filter(video__id=video_id).values('content','user__userinfo__user_name','user__userinfo__user_icon__icon_img','question_video__id','qv_date')
    qvs_list = list(qvs)
    for i in range(len(qvs_list)):
        qvs_list[i]['qv_date'] = qvs_list[i]['qv_date'].strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(json.dumps(qvs_list))





def insert_user_courseware(request):
    '''
    添加用户课件
    :param request:  user_id  courseware_id iswatch=1
    :return:
    '''
    user_id = request.GET.get('user_id')
    courseware_id = request.GET.get('courseware_id')
    user_f = User.objects.filter(id=user_id).first()
    courseware_f = Courseware.objects.filter(id=courseware_id).first()
    res = None
    try:
        UserCourseware.objects.create(user=user_f, courseware=courseware_f, iswatch=1)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        return HttpResponse(json.dumps({"result": res}))





def get_user_courseware(request):
    '''
    查询用户课件
    :param request:  user_id  courseware_id
    :return: iswatch【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    courseware_id = request.GET.get('courseware_id')
    iswatch = UserCourseware.objects.filter(user__id=user_id, courseware__id=courseware_id).values('iswatch')
    if iswatch:
        iswatch = iswatch[0]['iswatch']
    else:
        iswatch = 0
    return HttpResponse(json.dumps({"iswatch": iswatch}))




def insert_question_courseware(request):
    '''
    添加用户对某课件的提问
    :param request: content  user_id  courseware_id question_courseware_id
    :return:
    '''
    content = request.GET.get('content')
    user_id = request.GET.get('user_id')
    courseware_id = request.GET.get('courseware_id')
    question_courseware_id = request.GET.get('question_courseware_id')
    user_f = User.objects.filter(id=user_id).first()
    courseware_f = Courseware.objects.filter(id=courseware_id).first()
    res = None
    try:
        if question_courseware_id:
            question_courseware_f = QuestionCourseware.objects.filter(id=question_courseware_id).first()
            QuestionCourseware.objects.create(content=content, courseware=courseware_f, user=user_f, question_courseware=question_courseware_f)
        else:
            QuestionCourseware.objects.create(content=content, courseware=courseware_f, user=user_f)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        return HttpResponse(json.dumps({"result": res}))




def get_question_courseware(request):
    '''
    查询某课件的所有用户提问
    :param request: courseware_id
    :return: content user_info_icon user_info_name question_courseware qc_date【Json字符串】
    '''
    courseware_id = request.GET.get('courseware_id')
    qvs = QuestionCourseware.objects.filter(courseware__id = courseware_id).values('content','user__userinfo__user_icon__icon_img','user__userinfo__user_name','question_courseware__id','qc_date')
    qvs_list = list(qvs)
    for i in range(len(qvs_list)):
        qvs_list[i]['qc_date'] = qvs_list[i]['qc_date'].strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(json.dumps(qvs_list))
