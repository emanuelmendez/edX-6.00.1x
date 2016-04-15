import random

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
    def get_number_of_species(self, animal):
        return self.species_types[animal]    
    def get_location(self):
        location = (float(self.location[0]), float(self.location[1]))
        return location
    def get_species_count(self):
        species_types_copy = {}
        for animal in self.species_types:
            if self.species_types[animal] > 0:
                species_types_copy[animal] = self.species_types[animal]
        return species_types_copy
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if species in self.species_types:
            self.species_types[species] -= 1


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name 
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        score = 1.0 * num_desired
        return score


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        num_other = 0
        for animal in adoption_center.species_types:
            if adoption_center.species_types[animal] > 0 and animal in self.considered_species:
                num_other += adoption_center.species_types[animal]
        return Adopter(self.name, self.desired_species).get_score(adoption_center) + 0.3 * num_other

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
        
    def get_score(self, adoption_center):
        num_other = 0
        if self.feared_species in adoption_center.species_types:
            num_other += adoption_center.species_types[self.feared_species]
        score = Adopter(self.name, self.desired_species).get_score(adoption_center) - 0.3 * num_other 
        if score >= 0:
            return score
        else:
            return 0.0
            
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        
    def get_score(self, adoption_center):
        for animal in adoption_center.species_types:
            if animal in self.allergic_species and adoption_center.species_types[animal] > 0:
                return 0.0
        
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        score = 1.0 * num_desired
        return score

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most 
    allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter 
    is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, 
    and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        lowest = 1.0
        
        for animal in adoption_center.species_types:
            if animal in self.allergic_species and adoption_center.species_types[animal] > 0:
                if self.medicine_effectiveness[animal] < lowest:
                    lowest = self.medicine_effectiveness[animal]
        
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        score = num_desired * lowest
        return score
    

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
        
    def get_linear_distance(self, to_location):
        import math 
        distance = math.sqrt((to_location[0] - self.location[0])**2 + (to_location[1] - self.location[1])**2)
        return distance
        
    def get_score(self, adoption_center):
        random_value = 1.0
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance >= 5.0:
            random_value = random.uniform(0.1, 0.5)
        elif distance >= 3.0:
            random_value = random.uniform(0.5, 0.7)
        elif distance >= 1.0:
            random_value = random.uniform(0.7, 0.9)
            
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        score = random_value * num_desired
        return score
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    Returns a list of an organized adoption_center such that the scores for 
    each AdoptionCenter to the Adopter will be ordered from highest score to 
    lowest score. In case of ties, order the adoption center names alphabetically.
    """
    list_of_adoption_centers = sorted(list_of_adoption_centers, key=lambda x:x.get_name())
    return sorted(list_of_adoption_centers, key=lambda x:adopter.get_score(x),reverse = True)
    
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    returns a list of the top n scoring Adopters from 
    list_of_adopters (in numerical order of score). 
    In case of ties, order the Adopter names alphabetically.
    """
    list_of_adopters = sorted(list_of_adopters, key=lambda x:x.get_name())
    ordered_list = sorted(list_of_adopters, key=lambda x:x.get_score(adoption_center),reverse = True)
    return ordered_list[:n]