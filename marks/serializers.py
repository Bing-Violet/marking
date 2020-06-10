from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('min_mark', 'max_mark', 'mean_mark', 'std_mark', 'count_mark', 'percentiles',)
		model = Result