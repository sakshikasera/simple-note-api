from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from notes.models import Note

class NoteAPITestCase(APITestCase):
    
    def test_create_note(self):
        url = reverse('note-create')
        data = {'title': 'Shadows of Eternity', 'body': 'A man discovers that every shadow holds a memory of the past, and unlocking them may reveal the key to immortality.'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Shadows of Eternity')
    
    def test_fetch_note_by_id(self):
        note = Note.objects.create(title='Shadows of Eternity', body='A man discovers that every shadow holds a memory of the past, and unlocking them may reveal the key to immortality.')
        url = reverse('note-detail', kwargs={'pk': note.pk})
        
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Shadows of Eternity')
    
    def test_query_notes_by_title_substring(self):
        Note.objects.create(title='Shadows of Eternity', body='A man discovers that every shadow holds a memory of the past, and unlocking them may reveal the key to immortality.')
        Note.objects.create(title='The Silent Hour', body='In a town where no one speaks after midnight, a woman must break the silence to save her family.')
        
        url = reverse('note-query')
        response = self.client.get(url, {'title': 'Shadows'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Shadows of Eternity')
    
    def test_update_note(self):
        note = Note.objects.create(title='Shadows of Eternity', body='In a town where no one speaks after midnight, a woman must break the silence to save her family.')
        url = reverse('note-update', kwargs={'pk': note.pk})
        data = {'title': 'The Forgotten Garden', 'body': 'Every flower in the garden blooms with a forgotten secret, waiting for someone brave enough to listen.'}
        
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_note = Note.objects.get(pk=note.pk)
        self.assertEqual(updated_note.title, 'The Forgotten Garden')
        self.assertEqual(updated_note.body, 'Every flower in the garden blooms with a forgotten secret, waiting for someone brave enough to listen.')

