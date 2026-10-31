"""Math helpers used by the Multi-Utility Toolkit."""

import math


def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    return math.factorial(number)


def compound_interest(principal, annual_rate, years, compounds_per_year=1):
    if principal < 0 or years < 0 or annual_rate <= -100 or compounds_per_year < 1:
        raise ValueError("Enter valid non-negative values and a positive compounding frequency.")
    amount = principal * (1 + annual_rate / (100 * compounds_per_year)) ** (compounds_per_year * years)
    return round(amount, 2), round(amount - principal, 2)


def trig(degrees):
    radians = math.radians(degrees)
    return {"sin": round(math.sin(radians), 4),
            "cos": round(math.cos(radians), 4),
            "tan": round(math.tan(radians), 4)}


def area(shape, *values):
    if shape == "circle" and len(values) == 1 and values[0] >= 0:
        return math.pi * values[0] ** 2
    if shape == "rectangle" and len(values) == 2 and min(values) >= 0:
        return values[0] * values[1]
    if shape == "triangle" and len(values) == 2 and min(values) >= 0:
        return values[0] * values[1] / 2
    if shape == "square" and len(values) == 1 and values[0] >= 0:
        return values[0] ** 2
    raise ValueError("Choose a supported shape and provide valid dimensions.")


def convert(value, conversion):
    factors = {
        "celsius_to_fahrenheit": (lambda x: x * 9 / 5 + 32),
        "fahrenheit_to_celsius": (lambda x: (x - 32) * 5 / 9),
        "km_to_miles": (lambda x: x * 0.621371),
        "miles_to_km": (lambda x: x / 0.621371),
        "kg_to_pounds": (lambda x: x * 2.20462),
        "pounds_to_kg": (lambda x: x / 2.20462),
    }
    try:
        return factors[conversion](value)
    except KeyError as error:
        raise ValueError("Unknown conversion.") from error
