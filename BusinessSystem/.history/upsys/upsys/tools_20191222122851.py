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