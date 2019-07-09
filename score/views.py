from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import logout
from .request import *
from .VerificationCode import verification_code_check
from .xlsread import *

# Create your views here.


def test(request):
    pass


def login_html(request):
    """返回登录界面"""
    login_status = request.session.get('login_status', 0)
    if login_status == 0:
        return render(request, 'login.html')
    else:
        return redirect('BPlan:index')


def login_check(request):
    """检查账户密码是否正确"""
    if request.method == 'POST':
        student_id = request.POST['student_id']
        student_password = request.POST['student_password']
        if verification_code_check(request):
            try:
                student = Student.objects.get(student_id__exact=student_id)
                if student_password == student.student_password:
                    request.session['login_status'] = 1
                    request.session['student_id'] = student.student_id
                    request.session['student_name'] = student.student_name
                    login_agent = get_agent(request)  # 获取登录的设备信息
                    ip = get_ip(request)  # 获取登录的ip
                    location = get_location(ip)  # 通过IP查询地理位置
                    login_record = LoginRecord.add_login_record(  # 增加一条登录记录
                        student,
                        login_ip=ip,
                        login_browser=login_agent['browser'],
                        login_system=login_agent['system'],
                        login_device=login_agent['device'],
                        login_location=location,
                    )
                    login_record.save()  # 保存登录记录
                    return HttpResponse("successLogin")  # 返回登录成功
                else:
                    return HttpResponse("passwordWrong")  # 返回密码错误
            except Student.DoesNotExist:
                return HttpResponse("idDoesNotExist")  # 返回用户不存在
        else:
            return HttpResponse('codeWrong')  # 返回验证码错误
    else:
        return redirect('BPlan:index')


def refresh6(request):
    """更新第六学期成绩"""
    student_list = read_excel_6(student_system="微电子科学与工程", xls_name="WDZ")
    for student in student_list:
        try:
            std = Student.objects.get(student_id__exact=student["student_id"])
        except Student.DoesNotExist:
            std = Student(student_id=student["student_id"])
        std.student_name = student["student_name"]
        std.student_system = System.objects.get(system_name=student["student_system"])
        std.academic_score_6 = student["academic_score_6"]
        std.credit_6 = student["credit_6"]
        std.student_identity = student["student_identity"]
        std.save()
    return HttpResponse('success')


def refresh1_5(request):
    """更新前5学期成绩"""
    student_list = read_excel_1_5(xls_name="WDZ")
    for student in student_list:
        try:
            std = Student.objects.get(student_id__exact=student["student_id"])
        except Student.DoesNotExist:
            std = Student(student_id=student["student_id"])
            std.student_system = System.objects.get(system_name='新成员')
        # std.student_name = student["student_name"]
        # std.student_system = System.objects.get(system_name=student["student_system"])
        std.developmental_score_1 = student["developmental_score_1"]
        std.developmental_score_2 = student["developmental_score_2"]
        std.developmental_score_3 = student['developmental_score_3']
        std.developmental_score_4 = student['developmental_score_4']
        std.developmental_score_5 = student['developmental_score_5']

        std.science_score_1 = student['science_score_1']
        std.science_score_2 = student['science_score_2']
        std.science_score_3 = student['science_score_3']
        std.science_score_4 = student['science_score_4']
        std.science_score_5 = student['science_score_5']

        std.academic_score_1_5 = student['academic_score_1_5']
        std.whole_score_1_5 = student['whole_score_1_5']
        std.credit_1_5 = student['credit_1_5']
        std.save()
    return HttpResponse('success')


def refresh_score(request):
    student_list = Student.objects.all()
    for student in student_list:
        student.credit_1_6 = student.credit_1_5 + student.credit_6
        student.academic_score_1_6 = (
            student.academic_score_6 * student.credit_6 +
            student.academic_score_1_5 * student.credit_1_5
        ) / student.credit_1_6
        student.whole_score_1_6 = (
            student.whole_score_1_5 * (student.credit_1_5+15) +
            student.academic_score_6 * student.credit_6 +
            student.developmental_score_6 * 1 +
            student.science_score_6 * 2
        ) / (student.credit_1_6+15+2+1)
        student.save()

    return HttpResponse('success')


def get_rank(request):
    student_id = request.GET.get('student_id')
    rank_type_list = [
        "-academic_score_1_5",
        "-academic_score_1_6",
        "-whole_score_1_5",
        "-whole_score_1_6",
    ]
    ranking = []

    student = Student.objects.get(student_id=student_id)
    student_list = Student.objects.filter(student_system=student.student_system)
    for rank_type in rank_type_list:
        ranking.append(list(student_list.order_by(rank_type).values_list('student_id', flat=True)).index(student_id)+1)

    return HttpResponse(ranking)
