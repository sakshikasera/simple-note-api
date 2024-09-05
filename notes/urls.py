from notes.views import NoteCreateView, NoteDetailView, NoteQueryView, NoteUpdateView
from django.urls import path
urlpatterns = [
    path('notes/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/',NoteDetailView.as_view(),name='note-detail'),
    path('notes/query/',NoteQueryView.as_view(), name='note-query'),
    path('notes/update/<int:pk>/',NoteUpdateView.as_view(), name='note-update'),
]
