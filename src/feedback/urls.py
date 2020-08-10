from django.urls import path

from .views import FeedbackView

app_name = "feedback"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    path('feedback/<int:pk>', FeedbackView.as_view()),
]
