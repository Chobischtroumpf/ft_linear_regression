import json

def read_theta():
    """
        Read the theta0 and theta1 from the file.
        Returns:
            theta0 (float): The theta0 value.
            theta1 (float): The theta1 value.
    """
    try :
        with open("theta.txt", "r") as f:
            theta = json.load(f)
            if len(theta) != 2:
                raise
    except Exception:
        print("Error: theta.txt not found or badly formated")
    return theta["theta0"], theta["theta1"]

def write_theta(theta0, theta1):
    """
        Write the theta0 and theta1 to the file.
        Args:
            theta0 (float): The theta0 value.
            theta1 (float): The theta1 value.
    """
    try:
        with open("theta.txt", "w") as f:
            json.dump({"theta0": theta0, "theta1": theta1}, fp)
    except Exception as e:
        print(e)

def  normalisedEstimatePrice(mileage):
    """
        Estimate the price of a car based on mileage.
        Args:
            mileage (int): The mileage of the car.
        Returns:
            int: The estimated price of the car as : theta0 + theta1 * mileage.
    """
    return theta0 + theta1 * mileage

def main():
    print("what mileage does your car have ?")
    mileage = None
    ask_again = True
    while ask_again:
        try:
            mileage = float(input(" car's mileage: ").strip().lstrip())
            ask_again = False
        except Exception:
            print("mileage has to be a number, ")

if __name__ == "__main__":
    main()