from django.apps import AppConfig


class StudentConfig(AppConfig):
    name = 'student'
    verbose_name=u'学生管理'        # 修改后台应用名称 __init__.py文件中也要添加默认config
