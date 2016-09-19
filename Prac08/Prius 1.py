
from Prac08.taxi import Taxi

def main():
    prius = Taxi("prius 1", 100)
    prius_drive = prius.drive(40)
    print("distance =", prius_drive)
    print("fare = $", prius.get_fare())

    prius.start_fare()
    prius_drive = prius.drive(100)
    prius_fare = prius.get_fare()
    print("distance = ", prius_drive)
    print("fare = $", prius_fare)


main()