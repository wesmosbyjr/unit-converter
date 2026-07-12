def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def miles_to_km(miles):
    return miles * 1.60934

def kg_to_lbs(kg):
    return kg * 2.20462

if __name__ == "__main__":
    temp = float(input("Enter temperature in Celsius: "))
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")

    distance = float(input("Enter distance in miles: "))
    print(f"{distance} miles = {miles_to_km(distance)} km")

    weight = float(input("Enter weight in kilograms: "))
    print(f"{weight} kg = {kg_to_lbs(weight)} lbs") 