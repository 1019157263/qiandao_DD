from django.contrib import admin

# Register your models here.



from .models import user,data,log_a


class log_aAdmin(admin.ModelAdmin):
    list_filter = ['time']#过滤器
    search_fields = ['username']
    
    list_display = ('name','username','time')





admin.site.register(user)

admin.site.register(data)
admin.site.register(log_a,log_aAdmin)
