from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =('id','name','sex','profession','email','qq','phone','status','created_time')
    list_filter = ('sex','status','created_time')
    search_fields = ('name','profession')
    # fieldsets=(
    #     ['base_info',{'fields':['name',('sex','profession'),('email','qq','phone'),'status']}],
    # )
    fieldsets = (
        (
            'base info',
            {'fields':
                 (
                     'name',
                     ('sex','profession'),
                     ('email','qq','phone'),
                     'status',
                 )
        }),
    )


admin.site.site_header='XX后台管理系统'  # 设置登陆页文字
admin.site.site_title='XX后台管理'    # 设置title上的文字
