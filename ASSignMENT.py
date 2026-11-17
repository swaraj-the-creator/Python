from abc import ABC,abstractmethod
class Remote(ABC):
    def dev_name(self,device):
        print("\nName of the device: ",device)
    def ONorOFF(self):
        pass
class TV(Remote):
    def ONorOFF(self):
        print("T.V. has switched ON")
class AC(Remote):
    def ONorOFF(self):
        print("A.C. has switched ON")
class MuSp(Remote):
    def ONorOFF(self):
        print("Music Speaker has switched ON\n")
tv = TV()
ac = AC()
mUsP = MuSp()
 
tv.dev_name("Living Room T.V.")
tv.ONorOFF()
 
ac.dev_name("Bedroom A.C.")
ac.ONorOFF()
 
mUsP.dev_name("Living Room Music Speaker")
mUsP.ONorOFF()

class SecCam:
    def status(self):
        print("Security Camera is on and recording")
 
class AnThSy:
    def status(self):
        print("Anti Thief System is active and working\n")
 
devs = [SecCam(), AnThSy()]

for dev in devs:
    dev.status()
