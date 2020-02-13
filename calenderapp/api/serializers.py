from rest_framework import serializers
from ..models import ScheduleEvent

class ScheduleEventSerializer(serializers.ModelSerializer):
    class Meta:
    	model = ScheduleEvent
    	fields = '__all__'