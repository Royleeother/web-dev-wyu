import time

contest_name_chinese = {
    'Contest1': '厅室申请',
    'Tiaozhancup': '挑战杯',
}

# 学院名 <--> 英文缩写
school_name_trans = {
    '经济管理学院': 'econ',
    '智能制造学部': 'cs',
    '政法学院': 'law',
    '文学院': 'lietra',
    '外国语学院': 'fore',
    '数学与计算科学学院': 'math',
    '应用物理与材料学院': 'phys',
    '土木建筑学院': 'civil',
    '生物科技与大健康学院': 'bio',
    '纺织材料与工程学院': 'weave',
    '艺术学院': 'art',
}

def getStatus(contest):
    """
    返回状态的中文字段 
    已通过
    正在审核
    审核不通过
    """
    status_dict = dict(
        is_pass = contest.is_pass,
        is_reviewing = contest.is_reviewing,
        is_fail = contest.is_fail,
    )
    status = dict(
        is_pass = '已通过',
        is_reviewing = '正在审核',
        is_fail = '审核不通过',
    )
    # for k, v in status_dict.items():
    #     print("current k:", k)
    #     print("current v:", v)
    #     if not v:
    #         return status[k]
    # 先来个土法炼钢，赶时间
    if status_dict['is_reviewing']:
        return status['is_reviewing']
    elif status_dict['is_pass']:
        return status['is_pass']
    else:
        return status['is_fail']

    # return '表单注册、或者审核的时候忘记改状态了！！！程序员出来挨打！！！'

from dashboard.models import Teacher
def they_are_teacher(tid_list):
    for tid in tid_list:
        tt = Teacher.objects.get(TID=tid)
        print("tt:", tt)
        tt.really_a_teacher = True
        tt.save()

def push_into_contest(user, contest_name):
    if user.contest == None:
        user.contest = '["{}"]'.format(contest_name)
    else:
        temp = eval(user.contest)
        print("temp before:", temp)
        temp.append(contest_name)
        print("temp after:", temp)
        user.contest = str(temp)
    user.save()

def throw_to_pool(user, pool):
    school = user.school
    what_school = school_name_trans[school]
    #
    temp = eval(getattr(pool, what_school))
    temp.append(str(user.user.id))
    #
    setattr(pool, what_school, str(temp)) 
    pool.save()

def current_time():
    time_struct = time.localtime()
    tt = '{}-{}-{}-{}:{}'.format(
        time_struct.tm_year, 
        time_struct.tm_mon, 
        time_struct.tm_mday, 
        time_struct.tm_hour, 
        time_struct.tm_min,
        )
    print("tt:", tt)   
    return tt

# 针对不同对象，给不同表单
def give_form():
    return

