import random
import string
import time
import zipfile
from pathlib import Path

# ============================================================
# FILE SETTINGS
# ============================================================

OUTPUT_TXT = Path("passwords.txt")
OUTPUT_ZIP = Path("passwords.zip")

# Character sets
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = string.punctuation
SPACE = " "


# ============================================================
# INPUT HELPERS
# ============================================================

def ask_yes_no(question):
    while True:
        answer = input(f"{question} [Y/N]: ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Please enter Y or N.")


def ask_int(question, minimum=1):
    while True:
        try:
            value = int(input(question))

            if value >= minimum:
                return value

        except ValueError:
            pass

        print(f"Enter a number >= {minimum}.")


# ============================================================
# PASSWORD GENERATION
# ============================================================

def make_password(characters, length):
    return "".join(random.choices(characters, k=length))


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("          PASSWORD TEST-DATA GENERATOR")
    print("=" * 60)

    # --------------------------------------------------------
    # Character selection
    # --------------------------------------------------------

    print("\nSelect character types:")

    use_lower = ask_yes_no("Lowercase letters")
    use_upper = ask_yes_no("Uppercase letters")
    use_numbers = ask_yes_no("Numbers")
    use_symbols = ask_yes_no("Symbols")
    use_spaces = ask_yes_no("Spaces")

    if not any([
        use_lower,
        use_upper,
        use_numbers,
        use_symbols,
        use_spaces
    ]):
        print("\nNo character types selected.")
        return

    # --------------------------------------------------------
    # Generation mode
    # --------------------------------------------------------

    print("\nGeneration modes:")
    print("1. Mixed selected characters")
    print("2. Alphabet only")
    print("3. Number only")
    print("4. Symbol only")
    print("5. Alphabet + Symbol")
    print("6. Alphabet + Number")
    print("7. Number + Symbol")
    print("8. Alphabet + Number + Symbol")
    print("9. Everything selected")

    while True:
        mode = input("\nMode [1-9]: ").strip()

        if mode in "123456789":
            break

        print("Choose a number from 1 to 9.")

    # --------------------------------------------------------
    # Length and amount
    # --------------------------------------------------------

    min_length = ask_int("\nMinimum length: ")

    max_length = ask_int(
        "Maximum length: ",
        min_length
    )

    amount = ask_int(
        "How many test strings to create: "
    )

    # --------------------------------------------------------
    # Build alphabet
    # --------------------------------------------------------

    alphabet = ""

    if use_lower:
        alphabet += LOWER

    if use_upper:
        alphabet += UPPER

    # --------------------------------------------------------
    # Select generation character set
    # --------------------------------------------------------

    if mode == "1":
        selected = alphabet

        if use_numbers:
            selected += NUMBERS

        if use_symbols:
            selected += SYMBOLS

        if use_spaces:
            selected += SPACE

    elif mode == "2":
        selected = alphabet

    elif mode == "3":
        selected = NUMBERS

    elif mode == "4":
        selected = SYMBOLS

    elif mode == "5":
        selected = alphabet + SYMBOLS

    elif mode == "6":
        selected = alphabet + NUMBERS

    elif mode == "7":
        selected = NUMBERS + SYMBOLS

    elif mode == "8":
        selected = alphabet + NUMBERS + SYMBOLS

    elif mode == "9":
        selected = alphabet + NUMBERS + SYMBOLS + SPACE

    if not selected:
        print("\nNo characters available for this mode.")
        return

    # --------------------------------------------------------
    # Display configuration
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("Starting generation")
    print("=" * 60)

    print(f"Characters available : {len(selected)}")
    print(f"Length               : {min_length}-{max_length}")
    print(f"Amount               : {amount:,}")
    print(f"Output               : {OUTPUT_TXT.resolve()}")

    print("\nGenerating...\n")

    # --------------------------------------------------------
    # STREAM DIRECTLY TO DISK
    # --------------------------------------------------------

    start_time = time.perf_counter()

    with OUTPUT_TXT.open(
        "w",
        encoding="utf-8",
        buffering=1024 * 1024
    ) as file:

        for i in range(amount):

            length = random.randint(
                min_length,
                max_length
            )

            password = make_password(
                selected,
                length
            )

            file.write(password + "\n")

            # Progress every 10,000 entries
            if (i + 1) % 10_000 == 0:

                elapsed = time.perf_counter() - start_time

                if elapsed > 0:
                    speed = (i + 1) / elapsed
                else:
                    speed = 0

                percent = ((i + 1) / amount) * 100

                print(
                    f"\r"
                    f"Progress: {percent:6.2f}% | "
                    f"Created: {i + 1:,}/{amount:,} | "
                    f"Speed: {speed:,.0f}/sec",
                    end="",
                    flush=True
                )

    # --------------------------------------------------------
    # GENERATION FINISHED
    # --------------------------------------------------------

    elapsed = time.perf_counter() - start_time

    if elapsed > 0:
        average_speed = amount / elapsed
    else:
        average_speed = 0

    print("\n\n" + "=" * 60)
    print("Generation complete")
    print("=" * 60)

    print(f"Created       : {amount:,}")
    print(f"Time          : {elapsed:.2f} seconds")
    print(f"Average speed : {average_speed:,.0f} strings/sec")
    print(f"TXT file      : {OUTPUT_TXT.resolve()}")

    # --------------------------------------------------------
    # CREATE ZIP
    # --------------------------------------------------------

    print("\nCreating ZIP...")

    zip_start = time.perf_counter()

    with zipfile.ZipFile(
        OUTPUT_ZIP,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=6
    ) as zip_file:

        zip_file.write(
            OUTPUT_TXT,
            arcname=OUTPUT_TXT.name
        )

    zip_elapsed = time.perf_counter() - zip_start

    print("\nZIP created successfully.")

    print(f"ZIP file      : {OUTPUT_ZIP.resolve()}")
    print(f"ZIP time      : {zip_elapsed:.2f} seconds")

    print("\nDone!")


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()
