# weather_format.py
"""Tiny script that converts Celsius to Fahrenheit.

Run with:
    python3 weather_format.py
"""
# 1️⃣ standard library import
from datetime import datetime

# 2️⃣ greet the user – demonstrate f-string & datetime
print(f"\n🌤️  Weather Formatter  — {datetime.utcnow().date()} (UTC)\n")

# 3️⃣ collect raw input (strings)
city = input("Enter city name: ")
celsius_raw = input("Enter temperature in °C: ")

# 4️⃣ convert to numeric type (float) so we can do math
celsius = float(celsius_raw)

# 5️⃣ calculate Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# 6️⃣ pretty-print the result
print(
    f"\nIn {city.title()}, {celsius:.1f}°C "
    f"is {fahrenheit:.1f}°F.\n"
)
