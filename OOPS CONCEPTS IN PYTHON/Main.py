from Vehicle import Bike, Car, Scooty

def main():
    Shine = Bike(colour= "Black", num_tyre=2, gears=5)
    Lambo = Car(colour= "Dark Blue", num_tyre=4, gears=6)
    Activa = Scooty(colour= "Serin Blue", num_tyre=2, gears=0)

    Lambo.display_details()
    print("\n")
    Shine.display_details()
    print("\n")
    Activa.display_details()

if __name__ == "__main__":
    main()