"""
Helper views for the debug_logger.
"""
from django.shortcuts import get_object_or_404
from django.views.generic import list_detail

from debug_logger.models import Request, Sql

def index(request):
    return list_detail.object_list(
        request,
        Request.objects.all().order_by('timestamp'),
        template_object_name='request',
    )

def sql_list(request, request_id):
    request_object = get_object_or_404(Request, pk=request_id)
    return list_detail.object_list(
        request,
        Sql.objects.filter(request=request_object).order_by('timestamp'),
        template_object_name='sql',
    )
