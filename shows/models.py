from django.db import models
from django.template.defaultfilters import slugify

# STATUS_CHOICES = (
#     ('C', 'Continuing'),
#     ('E', 'Ended'),
# )

class Show(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    actors = models.TextField()
    genre = models.CharField(max_length=100)
    # status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    status = models.CharField(max_length=15)
    imdb_id = models.CharField(max_length=15)
    zap2it_id = models.CharField(max_length=15)
    slug = models.SlugField()
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Show, self).save(*args, **kwargs)
    
    class Admin:
        pass