"""
    作者：王文浩   日期：2019/9/23 20:37
"""

def time_to_stamp(time_obj):
    '''
    :param time_obj: mysql time（mysql里的time格式）
    :return:  time_stamp （时间戳）
    '''
    time_obj_str = time_obj.strftime('%H:%M:%S')
    time_stamp = int(time_obj_str.split(':')[2]) + int(time_obj_str.split(':')[1]) * 60 + int(time_obj_str.split(':')[0]) * 60 * 60
    return time_stamp

def stamp_to_time(time_stamp):
    '''
    :param time_stamp:  time_stamp （时间戳，字符串）
    :return:  mysql time（mysql里的time格式）
    '''
    time_stamp = int(time_stamp) if time_stamp else 0
    time_obj = str(time_stamp // 60 // 60) + ":" + str(time_stamp % (60 * 60) // 60) + ":" + str(time_stamp % 60)
    return time_obj