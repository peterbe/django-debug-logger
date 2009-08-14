from django.contrib import admin

from debugger.models import Request, Sql

class RequestAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'method', 'absolute_path', 'status_code')
    ordering = ('timestamp',)

admin.site.register(Request, RequestAdmin)

admin.site.register(Sql)
