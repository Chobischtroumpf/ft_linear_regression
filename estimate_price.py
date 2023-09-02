# import numpy as np
# import matplotlib as mpl

def read_theta():
    """
        Read the theta0 and theta1 from the file.
        Returns:
            theta0 (float): The theta0 value.
            theta1 (float): The theta1 value.
    """
    try :
        with open("theta.txt", "r") as f:
            theta0 = float(f.readline())
            theta1 = float(f.readline())
    except Exception:
        print("Error: theta.txt not found")
    return theta0, theta1

def write_theta(theta0, theta1):
    """
        Write the theta0 and theta1 to the file.
        Args:
            theta0 (float): The theta0 value.
            theta1 (float): The theta1 value.
    """
    with open("theta.txt", "w") as f:
        f.write(str(theta0) + "\n")
        f.write(str(theta1) + "\n")

def  estimatePrice(mileage):
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