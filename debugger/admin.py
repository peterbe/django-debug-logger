from django.contrib import admin

from debugger.models import Request, Sql

admin.site.register(Request)
admin.site.register(Sql)
