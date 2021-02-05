from django.test import TestCase

# Create your tests here.
from rest_framework.test import RequestsClient

client = RequestsClient()

# on test l'application sur la classe etudiant
response = client.get('http://127.0.0.1:8000/etudiants/')
assert response.status_code == 200

response = client.get('http://127.0.0.1:8000/etudiants/1/')
assert response.status_code == 200


# on test l'application sur la classe enseignent
response = client.get('http://127.0.0.1:8000/enseignents/')
assert response.status_code == 200

response = client.get('http://127.0.0.1:8000/enseignents/1/')
assert response.status_code == 200

# on test l'application sur la classe specialites
response = client.get('http://127.0.0.1:8000/specialites/')
assert response.status_code == 200

response = client.get('http://127.0.0.1:8000/specialites/1/')
assert response.status_code == 200

# tester le departement
response = client.get('http://127.0.0.1:8000/departements/34/')
assert response.status_code == 404

import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Departement,Filiere
from .serializer import DepartementSerializer, FiliereSerializer
class DepartementTestCase(APITestCase):
    """ Test module for updating an existing departement record """

    def test_add_departement(self):
        data = {'nom':'pc', 'code':'pc'}
        response = self.client.post('/departements/',data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_listing_departement(self):
        response = self.client.get('/departements/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_retrieve_departement(self):

    #     response = self.client.get(reverse('/departements/', kwargs={'pk':1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
class FiliereTestCase(APITestCase):
    def test_listing_filiere(self):
        response = self.client.get('/filieres/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class EnseignentTestCase(APITestCase):
    def test_listing_enseignent(self):
        response = self.client.get('/enseignents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class SpecialiteTestCase(APITestCase):
    def test_listing_specialite(self):
        response = self.client.get('/specialites/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class ClasseTestCase(APITestCase):
    def test_listing_classe(self):
        response = self.client.get('/classes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      
class EtudiantTestCase(APITestCase):
    def test_listing_etudiant(self):
        response = self.client.get('/etudiants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)   
        
