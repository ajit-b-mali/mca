import requests
import json
from rich.console import Console
from rich.table import Table


console = Console()


API_KEY = "5f34ac90847e3668536f3182e1fc10df"
BASE_URL = "http://api.openweathermap.org/data/2.5"


default_json = {"city": "Kolhapur", "units": "metric"}


def get_weather(city, units="metric"):
    try:
        url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units={units}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error fetching weather data: {e}[/red]")
        return None


def save_preferences(city, units):
    with open("config.json", "w") as f:
        json.dump({"city": city, "units": units}, f)
        console.print("[green]Preferences saved![/green]")


def load_preferences():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return default_json


def display_weather(data, units):
    table = Table(title=f"Weather in {data['name']}", show_lines=True)
    table.add_column("Parameter", style="cyan", justify="left")
    table.add_column("Value", style="magenta", justify="right")

    table.add_row("Temperature", f"{data['main']['temp']}°{'C' if units == 'metric' else 'F'}")
    table.add_row("Feels Like", f"{data['main']['feels_like']}°")
    table.add_row("Humidity", f"{data['main']['humidity']}%")
    table.add_row("Description", data['weather'][0]['description'].capitalize())
    table.add_row("Wind Speed", f"{data['wind']['speed']} m/s")

    console.print(table)


def main():
    print("\n"*2)
    console.print(" Welcome to Terminal Weather-app ", style="bold red on blue")

    preferences = load_preferences()
    console.print(f"Default city: [blue]{preferences['city']}[/blue], Units: [blue]{preferences['units']}[/blue]")

    city = input(f"Enter city name (leave blank for {preferences['city']}): ") or preferences["city"]
    units = input("Units (metric/imperial, leave blank for default): ") or preferences["units"]

    weather_data = get_weather(city, units)
    if weather_data:
        display_weather(weather_data, units)

        if input("Save these as default? (y/N): ").lower() == "y":
            save_preferences(city, units)


if __name__ == "__main__":
    main()
