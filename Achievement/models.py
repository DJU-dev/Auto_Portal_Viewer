from django.db import models


class Private(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Figure(models.Model):        
    req_credit = models.CharField(max_length=10)
    acq_creidt = models.CharField(max_length=10)
    rating_cnt = models.CharField(max_length=10)
    r_scores = models.CharField(max_length=10) 
    r_scores_avg = models.CharField(max_length=10)
    per_score = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Semester(models.Model):
    classification = models.CharField(max_length=10)
    class_num = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    div_class = models.CharField(max_length=10) 
    grade = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    rating = models.CharField(max_length=10)
    def __str__(self):
        return self.name

# Create your models here.
