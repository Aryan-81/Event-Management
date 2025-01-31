from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsEvent_head  # Adjust the permissions accordingly
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

# Create your views here.

# View for Event
class EventView(APIView):
    permission_classes = [IsAuthenticated, IsEvent_head]  # Permissions for the event head
     
    def get(self, request):
        event_id = request.data.get('Event_id')# Retrieve event_id from query params
        
        if event_id:
            try:
                # Fetch the event using the event_id from query parameters
                event = Event.objects.get(Event_id=event_id)
                serializer = EventSerializer(event)
                return Response({'event': serializer.data})
            except Event.DoesNotExist:
                return Response({'msg': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Return all events if no event_id is provided
            
            return Response({'msg': "error"})
    def post(self, request):
        # Create a new event
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new event
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

