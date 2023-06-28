# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import MessageFront


class MessageView(APIView):
    queryset = MessageFront.objects.all()

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


