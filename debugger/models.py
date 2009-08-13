from django.db import models

class Request(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)
    method = models.CharField(max_length=7, blank=True)
    absolute_path = models.TextField(blank=True)
    status_code = models.IntegerField()
    response_size = models.IntegerField(null=True)

class Sql(models.Model):
    request = models.ForeignKey(Request)
    elapsed_time = models.IntegerField()
    sql = models.TextField(blank=True)
    executed_sql = models.TextField(blank=True)
    stacktrace = models.TextField(blank=True)
    timestamp = models.DateTimeField()
