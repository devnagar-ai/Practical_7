"""Basic text-file operations for the Multi-Utility Toolkit."""


def create_file(filename):
    """Create an empty file without overwriting an existing file."""
    try:
        with open(filename, "x", encoding="utf-8"):
            pass
        return f"Created {filename}."
    except FileExistsError:
        return f"{filename} already exists."
    except OSError as error:
        return f"File error: {error}"


def write_file(filename, text):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        return "File saved."
    except OSError as error:
        return f"File error: {error}"


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read() or "(File is empty.)"
    except OSError as error:
        return f"File error: {error}"


def append_file(filename, text):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        return "Text appended."
    except OSError as error:
        return f"File error: {error}"
