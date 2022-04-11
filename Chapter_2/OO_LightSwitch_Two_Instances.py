# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchisOn = False

    def turnOn(self):
        # turn the switch on
        self.switchisOn = True
    
    def turnOff(self):
        # turn the switch on
        self.switchisOn = False
    
    
    def show(self): # added for testing
        # turn the switch on
        print(self.switchisOn)    

# LightSwitch = LightSwitch() # ceate a LightSwitch instance
LightSwitch1 = LightSwitch()
LightSwitch2 = LightSwitch()




# Calls to methods
LightSwitch1.show()
LightSwitch2.show()
# Create instances
LightSwitch1.turnOn() # Turn switch 1 on

# Switch 2 should be off at start, but this makes it clearer
# Create instances
LightSwitch2.turnOff()
# Create instances
LightSwitch1.show()

# Create instances
LightSwitch2.show()
