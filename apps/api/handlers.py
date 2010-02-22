from django_website.apps import jobs
from django.shortcuts import get_object_or_404

from piston.handler import BaseHandler
from piston.utils import rc, validate

from django_website.apps.jobs.models import Job
from django_website.apps.jobs.forms import JobForm

class JobsHandler(BaseHandler):
    """ Handles REST communication """
    
    allowed_methods = ('GET', 'POST')
    model = Job
    
    def read(self, request, slug):
        # TODO import decorator allow_404 from pony-serve
        return get_object_or_404(Job, slug=slug)
    
    def create(self, request, slug):
        
        from django.contrib.auth.models import User
        user = User(username='test', email='toto@toto.com')#request.user
        user.save()
        
        job = Job(creator=user)
        form = JobForm(data=request.POST, instance=job)
        
        if form.is_valid():
            job = form.save()
            url = job.get_absolute_url()
            resp = rc.created
            resp.write('Job created')
        else:
            resp = rc.BAD_REQUEST
            resp.write('Invalid form')
        
        return resp