import random
from resources import roadside_encounter

# Travel Class to handle distance modifcations
class Travel:
    def __init__(self, dist):
        self.totalDistance    = int(dist)
        self.distanceTraveled = 0
        self.daysTraveled     = 0
        # Event Sets
        self.weather = ""
        # Flag for program completion
        self.travelcomplete   = 0
        
    # Move forward and see if encounter triggers
    def action(self):
        incriment = input(f"Day {self.daysTraveled} of travel. Distance traveled today (miles): ")
        self.RandWeather()
        print(f"Weather Today: {self.weather}")
        # Add distance for the day
        self.distanceTraveled += int(incriment)
        # Check for exit condition
        if (self.distanceTraveled >= self.totalDistance):
            self.travelcomplete = 1
            print(f"Travel complete.\nDays traveled: {self.daysTraveled}\n Miles traveled: {self.totalDistance}\n")
        # Check for event
        else:
            encounterSeed = random.randrange(100)
            if encounterSeed <= 30:
                # Picks a random event from the roadside encounters
                eventApprove = 0
                while eventApprove == 0:
                    # Pick time:
                    timeRand = random.randrange(100)
                    eventTime = ""
                    if (timeRand <= 15):
                        eventTime = "Morning"
                    elif(timeRand > 15 and timeRand <= 85):
                        eventTime = "Afternoon"
                    else:
                        eventTime = "Night"
                    # Pick event:
                    encounterPrompt = random.choice(list(roadside_encounter.event.values()))
                    print(f"Time: {eventTime}\nEvent: {encounterPrompt}\n")
                    # Approve generated event, else reroll
                    eventInquery = input("Approve? (y/n): ")
                    if (eventInquery == "y"):
                        eventApprove = 1
            else:
                print(f"Day {self.daysTraveled} passes by uneventfully.")
            # Incriment days
            self.daysTraveled += 1
    
    def RandWeather(self):
        pass
        
        
                

def main():
    # Run on open
    travelDone = 0
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Pathfinder Travel Tool (v0.1).")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    # Set up trip
    trip = Travel(travelDistInput())
    
    # Execute Travel loop
    while trip.travelcomplete == 0:
        trip.action()
    

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
            print(f"Estimated Travel time for {travelDistance}mi:\n30ft(24mi/day): {round(travelDistance/24, 2)} days\n20ft(16mi/day): {round(travelDistance/16, 2)}\n")
            travelConfrim = input("Does this sound right? (y/n): ")
            # Conformation
            if (travelConfrim == 'y'):
                conditionVerified = 1
        else:
            print("***Error***: Distance needs to be just numbers. You input a character!\n")
    
    return travelDistance

# Run
main()