from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('events/delete/<int:pk>/', views.event_delete, name='event_delete'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/participants/', views.participant_list, name='participant_list'),
    path('events/<int:event_id>/participants/create/', views.participant_create, name='participant_create'),
    path('participant/edit/<int:participant_id>/', views.participant_edit, name='participant_edit'),
    path('participant/delete/<int:participant_id>/', views.participant_delete, name='participant_delete'),
    path('events/<int:event_id>/import_participants/', views.import_participants, name='import_participants'),
    path('participant-template/', views.participant_template, name='participant_template'),
    path('export-events/', views.export_events, name='export_events'),
]
