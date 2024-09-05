from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Note
from .serializers import NoteSerializer


# Create your views here.

# Create Note
class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class =NoteSerializer

# Fetch Note by ID
class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Query Notes by Title Substring
class NoteQueryView(generics.ListAPIView):
    serializer_class = NoteSerializer
    def get_queryset(self):
        title_substring = self.request.query_params.get('title',None)
        if title_substring:
            return Note.objects.filter(title_icontains=title_substring)
        return Note.objects.all() 

# Update Note 
class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    


