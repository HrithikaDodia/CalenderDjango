from . import views
from django.urls import path
from .api import views as api

app_name = 'calenderapp'

urlpatterns = [
	path('create/', api.ScheduleEventCreateView.as_view(), name = 'api_create'),
	path('list/', api.ScheduleEventListView.as_view(), name = 'api_list'),
	path('update/<pk>/', api.ScheduleEventUpdateView.as_view(), name = 'api_update'),
	path('delete/<pk>/', api.ScheduleEventDeleteView.as_view(), name = 'api_delete'),
]