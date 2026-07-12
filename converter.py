def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def miles_to_km(miles):
    return miles * 1.60934

if __name__ == "__main__":
    temp = float(input("Enter temperature in Celsius: "))
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")