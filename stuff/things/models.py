import datetime
from decimal import Decimal

from django.db import models

class Thing(models.Model):
    '''Model for Things'''
    POOR = 'poor'
    AVERAGE = 'average'
    GOOD = 'good'
    EXCELLENT = 'excellent'
    CONDITION_CHOICES = (
        (POOR, POOR),
        (AVERAGE, AVERAGE),
        (GOOD, GOOD),
        (EXCELLENT, EXCELLENT),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default=AVERAGE)
    image = models.ImageField(upload_to='uploads/things/%Y/%m/%d/', blank=True)
        
    acquisition_date = models.DateTimeField(blank=True)
    disposition_date = models.DateTimeField(blank=True)
    story = models.TextField(blank=True)
    retail_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)

    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.id)
    
    class Meta:
        ordering = ['-created_ts']