from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('events/delete/<int:pk>/', views.event_delete, name='event_delete'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/participants/', views.participant_list, name='participant_list'),
    path('events/<int:event_id>/participants/create/', views.participant_create, name='participant_create'),
    path('participant/edit/<int:participant_id>/', views.participant_edit, name='participant_edit'),
    path('participant/delete/<int:participant_id>/', views.participant_delete, name='participant_delete'),
    path('events/<int:event_id>/import_participants/', views.import_participants, name='import_participants'),
    path('participant-template/', views.participant_template, name='participant_template'),
    path('export-events/', views.export_events, name='export_events'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    path('eventtypes/', views.eventtype_list, name='eventtype_list'),
    path('eventtypes/create/', views.eventtype_create, name='eventtype_create'),
    path('eventtypes/<int:pk>/edit/', views.eventtype_edit, name='eventtype_edit'),
    path('eventtypes/<int:pk>/delete/', views.eventtype_delete, name='eventtype_delete'),
]
