from django.db import models
import random
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100) 
    powers = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
  
def creating(use, nam, ori, pow, occ, eth):
    x = Character(user=use, name=nam, origin=ori, powers=pow, occupation=occ, ethnicity=eth)
    x.save()
    return x


def viewing_all():
    liszt = [] 
    for character in Character.objects.all():
        liszt.append(character)
    return liszt

def searching(name):
    for character in viewing_all():
        if character.name == name:
            return character

def updating(nam, category, content):
    character = searching(nam)
    if category == "name":
        character.name = content
        character.save()
    elif category == "origin":
        character.origin = content
        character.save()
    elif category == "powers":
        character.powers = content
        character.save()
    elif category == "occupation":
        character.occupation = content
        character.save()
    elif category == "ethnicity":
        character.ethnicity = content
        character.save()
    

def random_character():
    random_name = random.randint(0, 11)
    if random_name == 0:
      random_name = 'Michael Jackson'
    elif random_name == 1:
      random_name = 'Franz Liszt'
    elif random_name == 2:
      random_name = 'Curious George'
    elif random_name == 3:
      random_name = 'Weepingbell'
    elif random_name == 4:
      random_name = 'Bob Ross'
    elif random_name == 5:
      random_name = 'Abraham Lincoln'
    elif random_name == 6:
      random_name = 'Kitune Napalm'
    elif random_name == 7:
      random_name = 'Scooby Dooby Dont'
    elif random_name == 8:
      random_name = 'Azazel Beelzebub'
    elif random_name == 9:
      random_name = 'Ananiah Anpu'
    elif random_name == 10:
      random_name = 'Neil DeGrase Tyson'
    elif random_name == 11:
      random_name = 'Snufkin'
      
    random_origin = random.randint(0,12)
    if random_origin == 0:
      random_origin = 'the Pillars of Creation at the center of the Universe'
    elif random_origin == 1:
      random_origin = 'Ohio'
    elif random_origin == 2:
      random_origin = 'the Dark Side of the Moon'
    elif random_origin == 3:
      random_origin = 'the Wastelands, home of the Buzzards and Bandits'
    elif random_origin == 4:
      random_origin = 'Mount Olympus, the Pantheon of the Gods'
    elif random_origin == 5:
      random_origin = 'the sacred grounds of the Garden of Eden'
    elif random_origin == 6:
      random_origin = 'the Lost City of Atlantis'
    elif random_origin == 7:
      random_origin = '1700s London, the time of the black plague'
    elif random_origin == 8:
      random_origin = 'the Pyramids of Giza in Egypt'
    elif random_origin == 9:
      random_origin = 'Weeping Hollow, the City of Zombies'
    elif random_origin == 10:
      random_origin = 'the Necropolis, city of the dead'
    elif random_origin == 11:
      random_origin = 'MoominValley'
    elif random_origin == 12:
      random_origin = 'The Edge of the Universe'

    random_occupation = random.randint(0, 12)
    if random_occupation == 0:
      random_occupation = 'Gunslinger'
    elif random_occupation == 1:
      random_occupation = 'Sorcerer Cult Leader'
    elif random_occupation == 2:
      random_occupation = 'Inter-Dimensional Astrophysicist'
    elif random_occupation == 3:
      random_occupation = 'Monsterologist'
    elif random_occupation == 4:
      random_occupation = 'Torturer of Souls'
    elif random_occupation == 5:
      random_occupation = 'Gatekeeper to the after-life'
    elif random_occupation == 6:
      random_occupation = 'God Machine known as the World Eater'
    elif random_occupation == 7:
      random_occupation = 'Timeline-Anomaly Detective'
    elif random_occupation == 8:
      random_occupation = 'Meta-physical Quantum Physicist'
    elif random_occupation == 9:
      random_occupation = 'Time Traveler'
    elif random_occupation == 10:
      random_occupation = 'Inter-Dimensional Beast Summoner'
    elif random_occupation == 11:
      random_occupation = 'Extra-Terrestrial Philanthropist'
    elif random_occupation == 12:
      random_occupation = 'who is also the long-lost, evil twin brother of Scooby Do'

    random_ethnicity = random.randint(0, 12)
    if random_ethnicity == 0:
      random_ethnicity = 'Regular Human'
    elif random_ethnicity == 1:
      random_ethnicity = 'Jackal Headed God'
    elif random_ethnicity == 2:
      random_ethnicity = 'Telepathic Ghost Cat'
    elif random_ethnicity == 3:
      random_ethnicity = 'Pocket Monster'
    elif random_ethnicity == 4:
      random_ethnicity = 'Anthropomorphic Fox Creature'
    elif random_ethnicity == 5:
      random_ethnicity = 'Highly Radioactive Frog'
    elif random_ethnicity == 6:
      random_ethnicity = 'Catboy'
    elif random_ethnicity == 7:
      random_ethnicity = 'Partially Digested Midget'
    elif random_ethnicity == 8:
      random_ethnicity = 'Demon Lord'
    elif random_ethnicity == 9:
      random_ethnicity = 'Boar Headed Monster'
    elif random_ethnicity == 10:
      random_ethnicity = 'Possessed Porcelain Marionette Doll'
    elif random_ethnicity == 11:
      random_ethnicity = 'Planet Sized Choir of Tortured Souls'
    elif random_ethnicity == 12:
      random_ethnicity = 'Throne, a galaxy-sized, primordial monster with an infinite number of eyes'

    random_powers = random.randint(0, 11)
    if random_powers == 0:
      random_powers = 'the Tsukuyomi, the Ultimate Telepathic Illusion Technique'
    elif random_powers == 1:
      random_powers = 'Playing the Piano really well'
    elif random_powers == 2:
      random_powers = 'Conjuration and Manipulation of Bones'
    elif random_powers == 3:
      random_powers = 'Time Dilation and Distortion'
    elif random_powers == 4:
      random_powers = 'Necromancy, raising the dead'
    elif random_powers == 5:
      random_powers = 'Inter-Dimensional Teleportation'
    elif random_powers == 6:
      random_powers = 'Immortality'
    elif random_powers == 7:
      random_powers = 'Summoner of Inter-Dimensional, Primordial Beasts'
    elif random_powers == 8:
      random_powers = 'Courage'
    elif random_powers == 9:
      random_powers = 'Shadow Configuration and Manipulation'
    elif random_powers == 10:
      random_powers = 'the Amaterasu, Telekinetic Combustion of Black Flames'
    elif random_powers == 11:
      random_powers = 'Granting any wish as long as an appropriate sacrifice is made to counter balance the wish'
    
    liszt = {
      "name": random_name, 
      "origin": random_origin, 
      "powers": random_powers, 
      "occupation": random_occupation, 
      "ethnicity": random_ethnicity
    }
    
    return liszt
    

