from django.db import models
from django.db.models import Min, Max, Avg, StdDev, Count, FloatField
import numpy

# Create your models here.


class Result(models.Model):
    test_id = models.IntegerField()
    scanned_on = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_number = models.IntegerField()
    mark = models.IntegerField()

    def percentiles(self):
    	results = Result.objects.values('mark')
    	result_array = []
    	for element in results:
    		result_array.append(element['mark'])
    	percentile_25 = numpy.percentile(result_array, 25)
    	percentile_50 = numpy.percentile(result_array, 50)
    	percentile_75 = numpy.percentile(result_array, 75)
    	return percentile_25, percentile_50, percentile_75

    @property
    def min_mark(self):
        return (Result.objects.aggregate(min_mark=Min('mark')))['min_mark']
    
    @property
    def max_mark(self):
        return (Result.objects.aggregate(max_mark=Max('mark')))['max_mark']
    
    @property
    def mean_mark(self):
        return (Result.objects.aggregate(avg_mark=Avg('mark')))['avg_mark']

    @property    
    def std_mark(self):
        return (Result.objects.aggregate(std_mark=StdDev('mark')))['std_mark']
    
    @property
    def count_mark(self):
        return (Result.objects.aggregate(count_mark=Count('mark')))['count_mark']



    # obtained = models.IntegerField()
    # available = models.IntegerField()

    # def calculate_mark(self):
    # 	return self.obtained/self.available*100
    # @property
    # def min_mark(self, test_number):
    #     return (Result.objects.filter(test_id=test_number).
    #     aggregate(min_mark=Min('mark')))['min_mark']

    # def max_mark(self, test_number):
    #     return (Result.objects.filter(test_id=test_number).
    #     aggregate(max_mark=Max('mark')))['max_mark']

    # def mean_mark(self, test_number):
    #     return (Result.objects.filter(test_id=test_number).
    #     aggregate(avg_mark=Avg('mark')))['avg_mark']

    # def std_mark(self, test_number):
    #     return (Result.objects.filter(test_id=test_number).
    #     aggregate(std_mark=StdDev('mark')))['std_mark']

    # def count_mark(self, test_number):
    #     return (Result.objects.filter(test_id=test_number).
    #     aggregate(count_mark=Count('mark')))['count_mark']

    # def percentiles(self, test_number):
    # 	results = Result.objects.filter(test_id=test_number).values('mark')
    # 	result_array = []
    # 	for element in results:
    # 		result_array.append(element['mark'])
    # 	percentile_25 = numpy.percentile(result_array, 25)
    # 	percentile_50 = numpy.percentile(result_array, 50)
    # 	percentile_75 = numpy.percentile(result_array, 75)
    # 	return percentile_25, percentile_50, percentile_75

