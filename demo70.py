class Ride:
    def fare(self):
        print("Fare: 100")
class LuxuryRide(Ride):
    def fare(self):
        print("Fare: 300")
ride_type = input().strip()
if ride_type == "LuxuryRide":
    ride = LuxuryRide()
else:
    ride = Ride()
ride.fare()