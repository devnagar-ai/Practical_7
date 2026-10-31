"""Menu-driven Multi-Utility Toolkit using Python's standard library."""

from datetime import datetime
import importlib
import random
import string
import time
import uuid

from toolkit_package import file_operations, math_utilities


def ask_int(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a number of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Enter a whole number.")


def ask_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")


def datetime_menu():
    while True:
        print("\nDate and Time\n1. Current date/time\n2. Days between dates\n3. Format a date\n4. Stopwatch\n5. Countdown\n0. Back")
        choice = input("Choose: ").strip()
        if choice == "0":
            return
        if choice == "1":
            now = datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M:%S (%A, %B %d, %Y)"))
        elif choice in {"2", "3"}:
            try:
                first = datetime.strptime(input("Date (YYYY-MM-DD): ").strip(), "%Y-%m-%d")
                if choice == "2":
                    second = datetime.strptime(input("Second date (YYYY-MM-DD): ").strip(), "%Y-%m-%d")
                    print(f"{abs((second - first).days)} days")
                else:
                    print(first.strftime("%A, %B %d, %Y"))
            except ValueError:
                print("Enter a valid date in YYYY-MM-DD format.")
        elif choice == "4":
            input("Press Enter to start; press Enter again to stop.")
            started = time.perf_counter()
            input()
            print(f"Elapsed: {time.perf_counter() - started:.2f} seconds")
        elif choice == "5":
            seconds = ask_int("Seconds: ", 1)
            try:
                while seconds:
                    print(f"{seconds} seconds remaining", end="\r", flush=True)
                    time.sleep(1)
                    seconds -= 1
                print("Time is up!                 ")
            except KeyboardInterrupt:
                print("\nCountdown stopped.")
        else:
            print("Choose a listed option.")


def math_menu():
    while True:
        print("\nMath\n1. Factorial\n2. Compound interest\n3. Trigonometry\n4. Shape area\n5. Unit conversion\n0. Back")
        choice = input("Choose: ").strip()
        try:
            if choice == "0":
                return
            if choice == "1":
                print(math_utilities.factorial(ask_int("Non-negative integer: ", 0)))
            elif choice == "2":
                principal = ask_float("Principal: ", 0)
                rate = ask_float("Annual rate (%): ", 0)
                years = ask_float("Years: ", 0)
                amount, interest = math_utilities.compound_interest(principal, rate, years)
                print(f"Final amount: {amount:.2f}; interest: {interest:.2f}")
            elif choice == "3":
                print(math_utilities.trig(ask_float("Angle in degrees: ")))
            elif choice == "4":
                shape = input("Shape (circle/rectangle/triangle/square): ").strip().lower()
                if shape in {"circle", "square"}:
                    dimensions = (ask_float("Radius: " if shape == "circle" else "Side: ", 0),)
                elif shape in {"rectangle", "triangle"}:
                    dimensions = (ask_float("Length/base: ", 0), ask_float("Width/height: ", 0))
                else:
                    raise ValueError("Unknown shape.")
                print(f"Area: {math_utilities.area(shape, *dimensions):.2f}")
            elif choice == "5":
                conversions = ["celsius_to_fahrenheit", "fahrenheit_to_celsius", "km_to_miles", "miles_to_km", "kg_to_pounds", "pounds_to_kg"]
                print("Conversions: " + ", ".join(conversions))
                name = input("Conversion: ").strip()
                value = ask_float("Value: ")
                print(f"Result: {math_utilities.convert(value, name):.2f}")
            else:
                print("Choose a listed option.")
        except ValueError as error:
            print(f"Invalid input: {error}")


def random_menu():
    while True:
        print("\nRandom Tools\n1. Integer\n2. Number list\n3. Password\n4. OTP\n5. Sample from values\n0. Back")
        choice = input("Choose: ").strip()
        if choice == "0":
            return
        elif choice == "1":
            low = ask_int("Minimum: ")
            high = ask_int("Maximum: ")
            if low <= high:
                print(random.randint(low, high))
            else:
                print("Minimum must not exceed maximum.")
        elif choice == "2":
            count = ask_int("How many numbers? ", 1)
            low = ask_int("Minimum: ")
            high = ask_int("Maximum: ")
            if low <= high:
                print([random.randint(low, high) for _ in range(count)])
            else:
                print("Minimum must not exceed maximum.")
        elif choice == "3":
            length = ask_int("Password length (at least 4): ", 4)
            alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
            chars = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice("!@#$%^&*")]
            chars.extend(random.choices(alphabet, k=length - 4))
            random.shuffle(chars)
            print("".join(chars))
        elif choice == "4":
            digits = ask_int("OTP digits: ", 1)
            print("".join(random.choices(string.digits, k=digits)))
        elif choice == "5":
            values = input("Enter values separated by commas: ").split(",")
            values = [value.strip() for value in values if value.strip()]
            if not values:
                print("Enter at least one value.")
                continue
            count = ask_int("Sample size: ", 1)
            if count <= len(values):
                print(random.sample(values, count))
            else:
                print(f"Sample size cannot exceed {len(values)}.")
        else:
            print("Choose a listed option.")


def uuid_menu():
    count = ask_int("How many UUIDs? ", 1)
    for _ in range(count):
        print(uuid.uuid4())


def file_menu():
    print("\nFile Tools\n1. Create\n2. Write/replace\n3. Read\n4. Append")
    choice = input("Choose: ").strip()
    filename = input("Text file path: ").strip()
    if not filename:
        print("File path cannot be empty.")
    elif choice == "1":
        print(file_operations.create_file(filename))
    elif choice == "2":
        print(file_operations.write_file(filename, input("Text to write: ")))
    elif choice == "3":
        print(file_operations.read_file(filename))
    elif choice == "4":
        print(file_operations.append_file(filename, input("Text to append: ")))
    else:
        print("Choose a listed option.")


def explore_module():
    available = {"datetime", "time", "math", "random", "uuid", "string"}
    name = input("Built-in module (datetime/time/math/random/uuid/string): ").strip()
    if name not in available:
        print("That module is not in the list.")
        return
    module = importlib.import_module(name)
    print(", ".join(dir(module)))


def main():
    while True:
        print("\n=== Multi-Utility Toolkit ===\n1. Date and time\n2. Math\n3. Random tools\n4. UUIDs\n5. File tools\n6. Explore a module\n0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!")
            return
        actions = {"1": datetime_menu, "2": math_menu, "3": random_menu,
                   "4": uuid_menu, "5": file_menu, "6": explore_module}
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Choose a listed option.")


if __name__ == "__main__":
    main()

