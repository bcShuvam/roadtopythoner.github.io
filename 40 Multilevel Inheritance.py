class ElectronicDeviec:
    feature = ["High Performance","Non-Portable"]

class PocketGadget(ElectronicDeviec):
    features = ["Low Performance","Portable"]
    def ft(self):
        return f"{self.feature[0]} and {self.feature[1]}"

class Phone(PocketGadget):
    AverageFeature = ["Medium Performance","Portable"]

Big = ElectronicDeviec()
Pocket = PocketGadget()
Phone = Phone()

print(Pocket.ft())