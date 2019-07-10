from django.contrib import admin

# Register your models here.

from .models import *


admin.site.site_header = '电光16查分系统后台'  # 网站登录页和H1
admin.site.site_title = '电光16查分系统后台'   # 网站标题


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'system_name',
        'system_student_num',
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'student_id',
        'student_name',
        'student_system',
        'student_identity',
        'change_time',
    ]

    search_fields = ['student_id', 'student_name']  # 搜索字段
    list_filter = ['student_system']
    list_per_page = 40


@admin.register(LoginRecord)
class LoginRecordAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'login_user',
        'login_ip',
        'login_browser',
        'login_system',
        'login_device',
        'login_location',
        'login_time',
    ]
    search_fields = ['login_user']
    date_hierarchy = 'login_time'  # 详细时间分层筛选
    list_per_page = 20

