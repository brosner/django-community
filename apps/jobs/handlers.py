from piston.handler import BaseHandler
from .models import Jobs

class JobsHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    model = Jobs
    
    def read(self, request):
        pass
    
    def create(self, request):
        pass