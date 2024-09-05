from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

# Create Note
class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Note created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Error creating note.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# Fetch Note by ID
class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def retrieve(self, request, *args, **kwargs):
        note = get_object_or_404(Note, pk=kwargs.get('pk'))
        serializer = self.get_serializer(note)
        return Response({
            "message": "Note retrieved successfully!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

# Query Notes by Title Substring
class NoteQueryView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', None)
        if title_substring:
            return Note.objects.filter(title__icontains=title_substring)
        return Note.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "message": "Notes retrieved successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "No notes found."
        }, status=status.HTTP_404_NOT_FOUND)

# Update Note 
class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def update(self, request, *args, **kwargs):
        note = get_object_or_404(Note, pk=kwargs.get('pk'))
        serializer = self.get_serializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Note updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Error updating note.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
