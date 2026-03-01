# pet_shelter.py - Pet Shelter Management System
# Starter code for e005-exercise-oop

"""
Pet Shelter Management System
-----------------------------
A system to manage animals in a pet shelter using OOP principles.

Class Hierarchy:
        Animal (Base Class)
       /       \
    Dog         Cat
   /   \          \
Puppy  ServiceDog  Kitten

Complete the TODO sections to finish the implementation.
"""


# =============================================================================
# Task 1: Base Animal Class
# =============================================================================

from unittest import case


class Animal:
    """Base class for all animals in the shelter."""
    
    def __init__(self, name, age, species):
        """
        Initialize an animal.
        
        Args:
            name: The animal's name
            age: Age in years
            species: Type of animal
        """
        self.name = name
        self.age = age
        self.species = species
        self._adopted = False  # Protected attribute
    
    def speak(self):
        """Make a sound. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement speak()")
    
    def describe(self):
        """Return a description of the animal."""
        status = "adopted" if self._adopted else "available"
        return f"{self.name} is a {self.age}-year-old {self.species} ({status})"
    
    def adopt(self):
        """Mark the animal as adopted."""
        if self._adopted:
            return f"{self.name} has already been adopted!"
        self._adopted = True
        return f"Congratulations! You adopted {self.name}!"
    
    def is_adopted(self):
        """Check if animal is adopted."""
        return self._adopted
    
    def __str__(self):
        """String representation."""
        return f"{self.species}: {self.name} (Age: {self.age})"


# =============================================================================
# Task 2: Dog and Cat Classes
# =============================================================================

class Dog(Animal):
    """A dog in the shelter."""
    
    def __init__(self, name, age, breed, is_trained=False):
        """
        Initialize a dog.
        
        Args:
            name: Dog's name
            age: Age in years
            breed: Dog breed (e.g., "Golden Retriever")
            is_trained: Whether the dog is house-trained
        """
        super().__init__(name, age, "Dog")
        self.breed = breed
        self.is_trained = is_trained
    
    def speak(self):
        """Dogs bark."""
        return f"{self.name} says Woof! Woof!"
    
    def fetch(self):
        """Dogs can fetch."""
        return f"{self.name} fetches the ball!"
    
    def describe(self):
        """Override to include breed and training."""
        base = super().describe()
        trained = "trained" if self.is_trained else "not trained"
        return f"{base} - {self.breed}, {trained}"


class Cat(Animal):
    """A cat in the shelter."""
    
    def __init__(self, name, age, color, is_indoor=True):
        """
        Initialize a cat.
        
        Args:
            name: Cat's name
            age: Age in years
            color: Cat's color/pattern
            is_indoor: Whether the cat is indoor-only
        """
        # calls parent constructor for name and age, sets color and indoor status afterward
        super().__init__(name, age, "Cat")
        self.color = color
        self.is_indoor = is_indoor

    def speak(self):
        """Cats meow."""
        return f"{self.name} says Meow!"
    
    def scratch(self):
        """Cats scratch."""
        return f"{self.name} scratches the furniture!"
    
    def describe(self):
        """Override to include color and indoor status."""
        # gets base description using super() parent class "Animal" then returns a string with color and indoor/outdoor status
        base_descriptor = super().describe()
        indoor_status = "indoor" if self.is_indoor else "outdoor"
        return f"{base_descriptor} - {self.color} {indoor_status} cat"


# =============================================================================
# Task 3: Specialized Classes
# =============================================================================

class Puppy(Dog):
    """A puppy (dog under 1 year old)."""
    
    def __init__(self, name, age_months, breed):
        """
        Initialize a puppy.
        
        Args:
            name: Puppy's name
            age_months: Age in months (not years!)
            breed: Puppy breed
        """
        # Convert months to years for parent
        age_years = age_months / 12
        super().__init__(name, age_years, breed, is_trained=False)
        self.age_months = age_months
    
    def speak(self):
        """Puppies yip."""
        return f"{self.name} says Yip! Yip!"
    
    def describe(self):
        """Show age in months for puppies."""
        status = "adopted" if self._adopted else "available"
        return f"{self.name} is a {self.age_months}-month-old {self.breed} puppy ({status})"


class ServiceDog(Dog):
    """A trained service dog."""
    
    def __init__(self, name, age, breed, service_type):
        """
        Initialize a service dog.
        
        Args:
            name: Dog's name
            age: Age in years
            breed: Dog breed
            service_type: Type of service (e.g., "guide", "therapy", "search")
        """
        # calls parent (dog) constructor with is_trained = true as per requiremnents, then sets service_type
        super().__init__(name, age, breed, is_trained=True)
        self.service_type = service_type
    
    def perform_service(self):
        """Perform the dog's service."""
        # Return "{name} performs {service_type} duties."
        return f"{self.name} performs {self.service_type} duties."
    
    def describe(self):
        """Include service type in description."""
        # Gets base description and add service type
        base = super().describe()
        return f"{base} - Service Type: {self.service_type}"


class Kitten(Cat):
    """A kitten (cat under 1 year old)."""
    
    def __init__(self, name, age_months, color):
        """
        Initialize a kitten.
        
        Args:
            name: Kitten's name
            age_months: Age in months
            color: Kitten's color/pattern
        """
        # Convert months to years
        age_years = age_months / 12
        # Store age_months
        self.age_months = age_months
        # calls parent constructor (Cat)
        super().__init__(name, age_years, color, is_indoor=False)
    
    def speak(self):
        """Kittens mew."""
        # Returns "{name} says Mew! Mew!"
        return f"{self.name} says Mew! Mew!"
    
    def describe(self):
        """Show age in months for kittens."""
        # Similar to Puppy.describe()
        status = "adopted" if self._adopted else "available"
        return f"{self.name} is a {self.age_months}-month-old {self.color} kitten ({status})"


# =============================================================================
# Task 4: The Shelter Class
# =============================================================================

class Shelter:
    """Manages the pet shelter."""
    
    def __init__(self, name):
        """Initialize the shelter."""
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):
        """Add an animal to the shelter."""
        self.animals.append(animal)
        return f"{animal.name} has been added to {self.name}"
    
    # self made function to remove animal for the interactive menu
    def remove_animal(self, name):
        """Remove an animal from the shelter by name."""
        animal = self.find_by_name(name)
        if animal:
            self.animals.remove(animal)
            return f"{animal.name} has been removed from {self.name}"
        return f"No animal named {name} found in {self.name}."
    

    def find_by_name(self, name):
        """Find an animal by name."""

        # loop through animals in the shelter (self.animals) and returns the animal that matches the name, if no match, returns None, case insensitive
        # assumes names are unique?
        for animal in self.animals:
            if animal.name.lower() == name.lower(): # Match found
                return animal
        return None # No match
    
    def list_available(self):
        """List all animals available for adoption."""
        # Returns a list of animals where is_adopted() is False
        return [animal for animal in self.animals if not animal.is_adopted()]
      
    def list_by_species(self, species):
        """List all animals of a specific species."""
        # Filters self.animals by species; case insensitive; return the list
        return [animal for animal in self.animals if animal.species.lower() == species.lower()]
    
    def adopt_animal(self, name):
        """Adopt an animal by name."""
        animal = self.find_by_name(name)
        if animal:
            return animal.adopt()
        return f"No animal named {name} found."
    
    def make_all_speak(self):
        """Demonstrate polymorphism - all animals speak."""
        print(f"\n--- {self.name} Choir ---")
        for animal in self.animals:
            print(f"  {animal.speak()}")
    
    def get_statistics(self):
        """Return shelter statistics."""
        total = len(self.animals)
        adopted = sum(1 for a in self.animals if a.is_adopted())
        available = total - adopted
        
        species_count = {}
        for animal in self.animals:
            species = animal.species
            species_count[species] = species_count.get(species, 0) + 1
        
        return {
            "total": total,
            "adopted": adopted,
            "available": available,
            "by_species": species_count
        }
    
    def display_all(self):
        """Display all animals."""
        print(f"\n{'='*50}")
        print(f"  {self.name} - Current Residents")
        print(f"{'='*50}")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.describe()}")
        print(f"{'='*50}")


# =============================================================================
# Task 5: Demonstration
# =============================================================================

def test_functionality():
    """Demonstrate the pet shelter system."""
    
    # Create shelter
    shelter = Shelter("Happy Paws Rescue")
    
    # Add various animals (using completed classes)
    shelter.add_animal(Dog("Buddy", 3, "Golden Retriever", True))
    # TODO: Add a Cat
    shelter.add_animal(Cat("Maya", 5, "Maine Coon", True))
    # TODO: Add a Puppy
    shelter.add_animal(Puppy("Rex", .5, "Labrador"))
    # TODO: Add a ServiceDog
    shelter.add_animal(ServiceDog("Rocky", 5, "German Shepherd", "guide-dog"))
    # TODO: Add a Kitten
    shelter.add_animal(Kitten("Nala", 7, "Calico"))
    
    # Display all animals
    shelter.display_all()
    
    # Demonstrate polymorphism
    shelter.make_all_speak()
    
    # Adopt an animal
    print("\n--- Adoption ---")
    print(shelter.adopt_animal("Buddy"))
    
    # Try to adopt again
    print(shelter.adopt_animal("Buddy"))
    
    # Show statistics
    stats = shelter.get_statistics()
    print(f"\n--- Shelter Statistics ---")
    print(f"  Total: {stats['total']}")
    print(f"  Available: {stats['available']}")
    print(f"  Adopted: {stats['adopted']}")
    print(f"  By Species: {stats['by_species']}")


def display_manu():
    print( f"""
--- Welcome to the Pet Shelter Management System ---
1. add animal to shelter
2. delete animal from shelter
3. list all animals in shelter
4. list all animals by species
5. list available animals for adoption
6. adopt an animal
7. make all animals speak
8. show shelter statistics
9. export shelter data
0. exit
----------------------------------------------------
""")
#
# Function to create an animal based on user input, code is long because we need to take into account multiple constructors and parameters
#
def make_animal(name, age, species):
    match species:
        case "Dog":
            breed = input("Enter dog breed: ")
            is_trained = input("Is the dog trained? (yes/no): ") == "yes"
            return Dog(name, age, breed, is_trained)
        case "Cat":
            color = input("Enter cat color/pattern: ")
            is_indoor = input("Is the cat indoor-only? (yes/no): ") == "yes"
            return Cat(name, age, color, is_indoor)
        case "Puppy":
            breed = input("Enter puppy breed: ")
            return Puppy(name, age * 12, breed)  # Convert years to months
        case "ServiceDog":
            breed = input("Enter service dog breed: ")
            service_type = input("Enter service type (e.g., guide, therapy): ")
            return ServiceDog(name, age, breed, service_type)
        case "Kitten":
            color = input("Enter kitten color/pattern: ")
            return Kitten(name, age * 12, color)  # Convert years to months
        case _:
            print("Unknown species, cannot create animal.")
            return None

def pretty_print_animals(animals):
    for animal in animals:
        print(f"    -{animal.describe()}")

def main():
    shelter = Shelter("Happy Paws Rescue 2")
    # Add various animals (using completed classes)
    shelter.add_animal(Dog("Buddy", 3, "Golden Retriever", True))
    shelter.add_animal(Cat("Maya", 5, "Maine Coon", True))
    shelter.add_animal(Puppy("Rex", .5, "Labrador"))
    shelter.add_animal(ServiceDog("Rocky", 5, "German Shepherd", "guide-dog"))
    shelter.add_animal(Kitten("Nala", 7, "Calico"))
    # Main function; will be used as interactive menu for users to manager shelter
    while True: # main loop
        display_manu()
        user_input = input("Enter Command >")
        match user_input:
            case "1":
                # add animal to shelter
                name = input("Enter animal name: ")
                age = float(input("Enter animal age (in years, enter months as decimals): "))
                species = input("Enter animal species (e.g., Dog, Cat; case-sensitive): ")
                animal = make_animal(name, age, species)
                if animal: # check to see if any errors in creating animal
                    shelter.add_animal(animal)
                    print("successfully added to shelter")
                else:
                    print("Error try again...")
                    continue
                
            case "2":
                # delete animal from shelter
                name = input("Enter the name of the animal to remove: ")
                result = shelter.remove_animal(name)
                print(result)
            case "3":
                # list all animals in shelter
                shelter.display_all()
            case "4":   
                # list all animals by species
                species = input("Enter species to filter by (e.g., Dog, Cat; case-sensitive): ")
                animals = shelter.list_by_species(species)
                print(f"Animals of species {species}:")
                pretty_print_animals(animals)
            case "5":
                # list available animals for adoption
                available_animals = shelter.list_available()
                print("Available animals for adoption:")
                pretty_print_animals(available_animals)
            case "6":
                # adopt an animal
                name = input("Enter the name of the animal to adopt: ")
                result = shelter.adopt_animal(name)
                print(result)
            case "7":
                # make all animals speak
                shelter.make_all_speak()
            case "8":
                # show shelter statistics, copied from old test function
                stats = shelter.get_statistics()
                print(f"\n--- Shelter Statistics ---")
                print(f"  Total: {stats['total']}")
                print(f"  Available: {stats['available']}")
                print(f"  Adopted: {stats['adopted']}")
                print(f"  By Species: {stats['by_species']}")
            case "9":
                # export shelter data
                file_name = input("Enter filename to export data: ")
                print("not implemented yet, try again letr..")
            case "0":
                print("Shutting down program...")
                break
            case _:
                print("Invalid command, try again...")
    
    
    


if __name__ == "__main__":
    #test_functionality()
    main()
