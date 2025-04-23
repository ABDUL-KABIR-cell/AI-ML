def main():
    while True:
        try:
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is {bmi:.2f} - {get_health_status(bmi)}")
        except ValueError:
            print("Please enter valid numbers.")

        again = input("Calculate for another person? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


main()
