from django.db import models

# Create your models here.


class System(models.Model):
    """专业"""
    system_name = models.CharField(max_length=10, verbose_name='专业名称')
    system_student_num = models.PositiveSmallIntegerField(verbose_name='人数')

    def __str__(self):
        return self.system_name

    class Meta:
        db_table = "System"
        ordering = ['-system_student_num']  # 以id为标准升序
        verbose_name_plural = '专业'


class Student(models.Model):
    """学生"""
    student_id = models.CharField(max_length=12, verbose_name='学号')
    student_name = models.CharField(max_length=12, verbose_name='姓名', default="")
    student_password = models.CharField(max_length=20, verbose_name='密码', default='ILoveEO16')
    student_system = models.ForeignKey(System, on_delete=models.CASCADE, verbose_name='专业')
    student_identity = models.CharField(max_length=12, verbose_name='备注信息', default='无')

    developmental_score_1 = models.FloatField(verbose_name='1学期发展成绩', default=0)
    science_score_1 = models.FloatField(verbose_name='1学期科创成绩', default=0)
    developmental_score_2 = models.FloatField(verbose_name='2学期发展成绩', default=0)
    science_score_2 = models.FloatField(verbose_name='2学期科创成绩', default=0)
    developmental_score_3 = models.FloatField(verbose_name='3学期发展成绩', default=0)
    science_score_3 = models.FloatField(verbose_name='3学期科创成绩', default=0)
    developmental_score_4 = models.FloatField(verbose_name='4学期发展成绩', default=0)
    science_score_4 = models.FloatField(verbose_name='4学期科创成绩', default=0)
    developmental_score_5 = models.FloatField(verbose_name='5学期发展成绩', default=0)
    science_score_5 = models.FloatField(verbose_name='5学期科创成绩', default=0)

    academic_score_6 = models.FloatField(verbose_name='6学期专业成绩', default=0)
    developmental_score_6 = models.FloatField(verbose_name='6学期发展成绩', default=0)
    science_score_6 = models.FloatField(verbose_name='6学期科创成绩', default=0)

    academic_score_1_5 = models.FloatField(verbose_name='前5学期专业成绩', default=0)
    whole_score_1_5 = models.FloatField(verbose_name='前5学期综合成绩', default=0)
    academic_score_1_6 = models.FloatField(verbose_name='前6学期专业成绩', default=0)
    whole_score_1_6 = models.FloatField(verbose_name='前6学期综合成绩', default=0)

    credit_1_5 = models.FloatField(verbose_name='前5学期学分', default=1)
    credit_6 = models.FloatField(verbose_name='第6学期学分', default=1)
    credit_1_6 = models.FloatField(verbose_name='前6学期学分', default=1)
    # ranking_1 = models.PositiveSmallIntegerField(verbose_name='前五学期综合排名')
    # ranking_2 = models.PositiveSmallIntegerField(verbose_name='前五学期纯专业成绩排名')
    # ranking_3 = models.PositiveSmallIntegerField(verbose_name='前六学期纯专业成绩排名')
    # ranking_4 = models.PositiveSmallIntegerField(verbose_name='（前五学期综合+第六学期专业）排名')
    change_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = "Student"
        ordering = ['student_id']  # 以id为标准升序
        verbose_name_plural = '学生'


class LoginRecord(models.Model):
    """用户的登录记录"""
    login_user = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='用户')
    login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, verbose_name='登录ip')
    login_browser = models.CharField(max_length=30, default='未知的浏览器', verbose_name='浏览器')
    login_system = models.CharField(max_length=30, default='未知的系统', verbose_name='操作系统')
    login_device = models.CharField(max_length=30, default='未知的设备', verbose_name='设备')
    login_location = models.CharField(max_length=30, default='未知位置', verbose_name='位置')
    login_time = models.DateTimeField(auto_now_add=True, verbose_name='登录时间')

    @classmethod
    def add_login_record(  # 增加一个访问记录
            cls,
            login_user,
            login_ip,
            login_browser,
            login_system,
            login_device,
            login_location,
    ):
        login_record = cls(
            login_user=login_user,
            login_ip=login_ip,
            login_browser=login_browser,
            login_system=login_system,
            login_device=login_device,
            login_location=login_location,
        )
        return login_record

    def __int__(self):
        return self.pk

    class Meta:
        db_table = "LoginRecord"
        ordering = ['-login_time']  # 以id为标准升序
        verbose_name_plural = '访问记录'


