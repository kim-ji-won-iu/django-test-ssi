from django.urls import path
from feedback.api.views import (
    api_detail_feedback_view,
    api_update_feedback_view,
    api_delete_feedback_view,
    api_create_feedback_view,

    ApiFeedbackListView,
    api_is_author_of_feedbackpost)

app_name = 'feedback'

urlpatterns = [
    path('<slug>/', api_detail_feedback_view, name="detail"),
    path('<slug>/update', api_update_feedback_view, name="update"),
    path('<slug>/delete', api_delete_feedback_view, name="delete"),
    path('create', api_create_feedback_view, name="create"),
    path('list', ApiFeedbackListView.as_view(), name="list"),
    path('<slug>/is_author', api_is_author_of_feedbackpost, name="is_author"),
]
