from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ScheduleEventSerializer
from ..models import ScheduleEvent

class ScheduleEventListView(ListAPIView):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleEventSerializer

class ScheduleEventCreateView(CreateAPIView):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleEventSerializer

class ScheduleEventUpdateView(UpdateAPIView):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleEventSerializer

class ScheduleEventDeleteView(DestroyAPIView):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleEventSerializer