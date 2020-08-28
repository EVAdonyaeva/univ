from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)

        return Response({"feedback": serializer.data})

    def post(self, request):
        feedback = request.data.get('feedback')
        # Create an feedback from the above data
        serializer = FeedbackSerializer(data=feedback)
        if serializer.is_valid(raise_exception=True):
            feedback_saved = serializer.save()

            return Response({"success": f"Feedback '{feedback_saved.theme}' created successfully"})


class FeedbackByIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        feedback = get_object_or_404(Feedback.objects.all(), pk=pk)
        data = request.data.get('feedback')
        serializer = FeedbackSerializer(instance=feedback, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            feedback_saved = serializer.save()

            return Response({
                "success": f"Feedback '{feedback_saved.theme}' updated successfully"
            })
