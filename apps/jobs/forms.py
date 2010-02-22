from models import Job

from django.forms import ModelForm

class JobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('slug', 'creation_date', 'creator')