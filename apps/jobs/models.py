from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Job(models.Model):
    """A job offer"""
    title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    offer_url = models.URLField(blank=True)
    creator = models.ForeignKey(User)
    slug = models.SlugField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
        

    
    class Meta:
        ordering = ['-creation_date']
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        slug = slugify(self.title)
        return ('job_detail', [self.slug])
        
    def save(self):
        self.slug = slugify(self.title)
        super(Job, self).save()