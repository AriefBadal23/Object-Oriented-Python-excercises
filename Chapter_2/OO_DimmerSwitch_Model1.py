# Dimmer Switch class

class DimmerSwitch():
    def __init__(self, label):
        # remember the data (state)
        self.label = label
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
        print('Label:' , self.label)
        print('Switch is on?', self.switchOn)
        print('Brightness is:', self.brightness)


# Main code
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

print('oDimmer1 variables:', vars(oDimmer1))

oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

oDimmer3 = DimmerSwitch('Dimmer3')

oDimmer1.show()
oDimmer2.show()
oDimmer3.show()
