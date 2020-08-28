from django.urls import path

from .views import FeedbackByIdView
from .views import FeedbackView

app_name = "feedback"

urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    path('feedback/<int:pk>', FeedbackByIdView.as_view()),
]
