from dose_calculator import calculate_dose
def main():
    print("Pediatric Dose Calculator")
    print("===========================")
    
    # Input medication name
    medication_name = input("Enter the medication name: ").strip()
    
    # Input weight
    while True:
        try:
            weight = float(input("Enter the child's weight (kg): "))
            if weight > 0:
                break
            else:
                print("Weight must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Calculate the dose
    result = calculate_dose(medication_name, weight)
    
    # Display the result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"\nMedication: {result['medication']}")
        print(f"Weight: {result['weight']} kg")
        print(f"Calculated Dose: {result['calculated_dose']} mg")
        if result['warning']:
            print(f"Warning: {result['warning']}")
        else:
            print("Dose is within safe limits.")

if __name__ == "__main__":
    main()
