from django.db import models
from django.db.models import Min, Max, Avg, StdDev, Count, FloatField

# Create your models here.
class Result(models.Model):
	test_id = models.IntegerField()
	scanned_on = models.DateTimeField(null=True, blank=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	student_number = models.IntegerField()
	obtained = models.IntegerField()
	available = models.IntegerField()

	@property
	def mark(self):
		return self.obtained/self.available*100

	def min_mark(self, test_number):
		return (Result.objects.filter(test_id=test_number).aggregate(Min('mark')))['mark__min']

	def max_mark(self, test_number):
		return Result.objects.filter(test_id=test_number).aggregate(Max('mark'))

	def mean_mark(self, test_number):
		return Result.objects.filter(test_id=test_number).aggregate(Avg('mark'))

	def std_mark(self, test_number):
		return Result.objects.filter(test_id=test_number).aggregate(StdDev('mark'))

	def count_mark(self, test_number):
		return Result.objects.filter(test_id=test_number).aggregate(Count('mark'))
