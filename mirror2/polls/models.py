from django.db import models

class Pdf(models.Model):
    link = models.CharField(max_length=255)
    data = models.FileField(null=False, blank=False,  upload_to='async-kv-table')
    description = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s %s" % (self.link, self.data, self.description)

    
 
