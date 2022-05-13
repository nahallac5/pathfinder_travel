import matplotlib as mp
import pandas as pd
from resources import roadside_encounter

# Travel Class to handle distance modifcations
class Travel:
    def __init__(self, dist):
        self.totalDistance = dist
        

def main():
    # Run on open
    travelDone = 0
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Pathfinder Travel Tool.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    # Set up trip
    trip = Travel(travelDistInput())
    
    #while travelDone == 0:
    #    pass
    

# User Input to 
def travelDistInput():
    conditionVerified = 0
    while conditionVerified == 0:
        # Read in milage
        travelDistance = input("Enter total travel distance in miles: ")
        # Verify milage
        if (travelDistance.isdecimal()):
            # Make sure its in int form, not str
            travelDistance = int(travelDistance)
            # Travel Estimate
            print(f"Estimated Travel time for {travelDistance}mi:\n30ft max(24mi/day): {travelDistance/24} days\n20ft(16mi/day) max: {travelDistance/16}\n")
            travelConfrim = input("Does this sound right? (y/n): ")
            # Conformation
            if (travelConfrim == 'y'):
                conditionVerified = 1
        else:
            print("***Error***: Distance needs to be just numbers. You input a character!\n")
    
    return travelDistance

main()