from django.test import TestCase
from app.models import *

# Create your tests here.


class TestState(TestCase):
    def test_can_create(self):
        contact = creating(
            "tim",
            "a toxic ocean volcano",
            "immortality",
            "space explorer",
            "tardigrade",
        )
        
        self.assertEqual(contact.id, 1)
        self.assertEqual(contact.name, "tim")
        self.assertEqual(contact.origin, "a toxic ocean volcano")
        self.assertEqual(contact.powers, "immortality")
        self.assertEqual(contact.occupation, "space explorer")
        self.assertEqual(contact.ethnicity, "tardigrade")

    def test_viewing_all(self):
        creating(
            "tim",
            "a toxic ocean volcano",
            "immortality",
            "space explorer",
            "tardigrade",
        ) 
        creating(
            "Ananiah",
            "Ancient Egypt",
            "ghost powers",
            "ghost boy",
            "Egyptian",
        ) 
        all_ = viewing_all()
        self.assertEqual(len(all_), 2)

    def test_searching(self):
        tardigrade = creating(
            "tim",
            "a toxic ocean volcano",
            "immortality",
            "space explorer",
            "tardigrade",
        ) 
        creating(
            "Ananiah",
            "Ancient Egypt",
            "ghost powers",
            "ghost boy",
            "Egyptian",
        ) 
        tim = searching("tim")
        ana = searching("Ananiah")
        self.assertNotEqual(tim, ana)
        self.assertEqual(tim, tardigrade)
        self.assertEqual(tim.name, "tim")
        self.assertEqual(ana.name, "Ananiah")

    def test_updating(self):
        creating(
            "tim",
            "a toxic ocean volcano",
            "immortality",
            "space explorer",
            "tardigrade",
        ) 
        creating(
            "Ananiah",
            "Ancient Egypt",
            "ghost powers",
            "ghost boy",
            "Egyptian",
        ) 

        updating("tim", "origin", "unknown")
        tardigrade = searching("tim")
        self.assertEqual(tardigrade.origin, "unknown")
        updating("Ananiah", "occupation", "he who guides souls to the after life")
        niah = searching("Ananiah")
        self.assertEqual(niah.occupation, "he who guides souls to the after life")

    def test_deleting(self):
        creating(
            "Ananiah",
            "Ancient Egypt",
            "ghost powers",
            "ghost boy",
            "Egyptian",
        ) 

        self.assertEqual(len(Character.objects.all()), 1)
        deleting("Ananiah")
        self.assertEqual(len(Character.objects.all()), 0)