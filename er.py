from abc import ABC, abstractmethod 
print(" me    b")
print("\n\n\n\n\n\nTHIS IS AN ABANDONED PROGRAM")
class SmartDevice(ABC):

    def show_device(self, name):
        print("De ce    e:", name)

    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def turn_on(self):
        print("S art Li t is now ON")
 
 
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Sm rt  an  s now ON")
 
 
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart Speaker is     ON")

light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()
 
light.show_device("Liv ng Room Ligh ")
light.turn_on()
 
fan.show_device("Bedroo  Fan")
fan.turn_on()
 
speaker.show_device("Mus   Spea r")
speaker.turn_on()

class SecurityCamera:
    def check_status(self):
        print("Security  Camera  s recording")
 
 
class DoorLock:
    def        atus(self):
        print("D or L ck is secure")

#                             rLock()]




 
#or device in devices:
    #device.check_status()
 
print("========= ==============    ==")
