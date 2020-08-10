from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.Serializer):
    theme = serializers.CharField(max_length=120)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)

    def update(self, feedback, validated_data):
        feedback.theme = validated_data.get('title', feedback.theme)
        feedback.description = validated_data.get('description', feedback.description)
        feedback.email = validated_data.get('body', feedback.email)
        feedback.save()

        return feedback
