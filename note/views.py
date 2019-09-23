from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('note...index...')


def get_note(request):
    '''
    获取 note
    :param request:  user_id
    :return: id   title   content_editor   publish_date   classify   mold 【Json字符串】
    '''
    pass

def get_note_number(request):
    '''
    获取 笔记个数
    :param request: user_id
    :return: note_num 【Json字符串】
    '''
    pass


def get_note_info(request):
    '''
    获取笔记详情
    :param request:  note_id
    :return: title  content_html  content_editor  publish_date classify  mold 【Json字符串】
    '''
    pass

def update_note_info(request):
    '''
    修改笔记
    :param request: note_id
    :return:
    '''
    pass

def insert_note_info(request):
    '''
    添加笔记
    :param request: user_id
    :return:
    '''
    pass

def delete_note(request):
    '''
    删除笔记
    :param request:
    :return:
    '''
    pass