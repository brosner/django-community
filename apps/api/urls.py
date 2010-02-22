from django.conf.urls.defaults import *

from piston.resource import Resource
from . import handlers

urlpatterns = patterns('',
    url(r'jobs/(?P<slug>[\w-]+)$',
        Resource(handlers.JobsHandler),
        name = 'job_detail')
)