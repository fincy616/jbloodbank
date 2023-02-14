from django.contrib import admin
from .models import User, Blood_Request, email_id
# Register your models here.
class UserReg(admin.ModelAdmin):
    list_display= ('uid','full_name','email','address','phn_no','height','weight','pincode','blood_group','gender')
    search_fields = ('blood_group','pincode','gender')
    list_filter = ('blood_group','gender','pincode',)
admin.site.register(User,UserReg)

class BreqReg(admin.ModelAdmin):
    list_display= ('p_name','p_gender','p_hospitalname','p_bystander','p_phn_number','p_bloodgroup','p_unit','p_bloodneed','p_reqstudent')
    search_fields = ('p_bloodgroup','p_gender','p_hospitalname')
    list_filter = ('p_bloodgroup','p_gender','p_hospitalname',)
admin.site.register(Blood_Request, BreqReg)

class emailReg(admin.ModelAdmin):
    list_diaplay = ('mail_id')
admin.site.register(email_id, emailReg)
