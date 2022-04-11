# Dimmer Switch class

class DimmerSwitch():
    def __init__(self):
        # remember the data (state)
        self.switchOn = False
        self.brightness = 0

    # The behaviours
    def turnOn(self):
        self.switchOn = True
    
    def turnOff(self):
        self.switchOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1


    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness -1


    def show(self):
        print('Switch is on?', self.switchOn)
        print('Brightness is:', self.brightness)


# Main code
oDimmer = DimmerSwitch()

# Turn switch on, and raise the level 5 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()


# Lower the level 2 times, and turn switch off
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()


# Turn switch on, and raise the level 3 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

