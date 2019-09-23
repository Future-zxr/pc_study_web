from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('user...index...')


def get_user(request):
    '''
    获取 User ：用户基本信息
    :param request: user_id 或 user_tel
    :return:  id tel   psw   register_time 【Json字符串】
    '''
    pass


def get_user_info(request):
    '''
    获取 UserInfo ：用户信息
    :param request: user_id
    :return:  user_name  user_icon__icon_img   user_sex__name  identity  address introduce【Json字符串】
    '''
    pass


def get_user_integral(request):
    '''
    获取 UserIntegral ：用户积分
    :param request: user_id
    :return: integral_sum 【Json字符串】
    '''
    pass

def update_user_icon(request):
    '''
    修改用户头像
    :param request: user_id  user_icon
    :return:修改状态
    '''
    pass

def update_user_info(request):
    '''
    修改用户资料
    :param request: user_name  user_sex（1/3）  identity  address introduce【Json字符串】
    :return:修改状态
    '''
    pass


def update_user_psw(request):
    '''
    修改用户密码
    :param request: user_id  user_psw
    :return:修改状态
    '''
    pass

def update_user_email(request):
    '''
    修改用户邮箱
    :param request: user_id  user_email
    :return:修改状态
    '''
    pass

def insert_integral(request):
    '''
    添加用户积分
    :param request: user_id  integral
    :return: 插入状态
    '''
    pass


def insert_checkin(request):
    '''
    用户签到，并 调用insert_integral() 向 UserIntegral 加入 2 积分
    :param request: user_id  now_day（今天日期）
    :return: 签到状态（已签到、签到成功、签到失败）
    '''
    pass


def get_teacher(request):
    '''
    获取老师信息
    :param request: course_id（为空则无条件选择10个）
    :return: id name introduce  teacher_icon  teacher_sex  teacher_identity【Json字符串】
    '''
    pass