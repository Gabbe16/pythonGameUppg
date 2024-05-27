# Import statements
import requests

# Function to get the temperature
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        return temperature
    else:
        print("City not found.")

def main():
    city = input("Enter city name: ")
    api_key = "f3766672014224dca721272a510aec96"  # Replace this with your actual API key
    get_weather(city, api_key)

if __name__ == "__main__":
    main()

# Function to get the temperature to then get the color
def get_temp():
    city = input("Enter city name: ")
    api_key = "f3766672014224dca721272a510aec96"
    temp = get_weather(city, api_key)
    print(temp)
    temp = round(temp)
    if temp >= 30:
        color = (139, 64, 0)
        return color
    elif temp >= 20:
        color = (204, 85, 0)
        return color
    elif temp >= 0:
        color = (255, 255, 255)
        return color
    elif temp < 0:
        color = (0, 0, 255)
        return color
