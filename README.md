# Password Test-Data Generator

A simple, interactive command-line tool for generating large volumes of random password-like test strings.  
Useful for testing password strength checkers, authentication systems, hashing performance, or any application that needs realistic password datasets.

---

## Features

- **Flexible character selection**  
  Choose any combination of:
  - Lowercase letters (`a-z`)
  - Uppercase letters (`A-Z`)
  - Numbers (`0-9`)
  - Symbols (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`)
  - Spaces

- **Multiple generation modes**
  1. Mixed selected characters
  2. Alphabet only
  3. Numbers only
  4. Symbols only
  5. Alphabet + Symbols
  6. Alphabet + Numbers
  7. Numbers + Symbols
  8. Alphabet + Numbers + Symbols
  9. Everything selected (including spaces)

- **Configurable length range** – Set minimum and maximum password length
- **High-volume generation** – Create thousands or millions of strings efficiently
- **Streaming write** – Writes directly to disk with buffered I/O for low memory usage
- **Progress reporting** – Real-time progress, speed, and percentage updates
- **Automatic ZIP packaging** – Creates a compressed `passwords.zip` containing the generated file

---

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only the standard library)

---

## Installation

1. Clone the repository or download the script:

```bash
git clone [https://github.com/yourusername/password-test-data-generator.git
cd password-test-data-generator](https://github.com/HafizIbrahimSuriya/Password-Test-Data-Generator)
```

2. (Optional) Make the script executable:

```bash
chmod +x Password-Test-Data-Generator.py
```

---

## Usage

Run the script:

```bash
python Password-Test-Data-Generator.py
```

or

```bash
python3 Password-Test-Data-Generator.py
```

### Interactive Steps

1. Select which character types to include (Y/N for each).
2. Choose a generation mode (1–9).
3. Enter the minimum password length.
4. Enter the maximum password length.
5. Enter how many test strings to generate.

The tool will then generate the passwords, display progress, and create two files in the current directory:

- `passwords.txt` – One password per line
- `passwords.zip` – Compressed archive of the text file

---

## Example Session

```
============================================================
          PASSWORD TEST-DATA GENERATOR
============================================================

Select character types:
Lowercase letters [Y/N]: y
Uppercase letters [Y/N]: y
Numbers [Y/N]: y
Symbols [Y/N]: n
Spaces [Y/N]: n

Generation modes:
1. Mixed selected characters
2. Alphabet only
3. Number only
4. Symbol only
5. Alphabet + Symbol
6. Alphabet + Number
7. Number + Symbol
8. Alphabet + Number + Symbol
9. Everything selected

Mode [1-9]: 6

Minimum length: 8
Maximum length: 16
How many test strings to create: 100000

============================================================
Starting generation
============================================================
Characters available : 62
Length               : 8-16
Amount               : 100,000
Output               : /path/to/passwords.txt

Generating...

Progress: 100.00% | Created: 100,000/100,000 | Speed: 185,432/sec

============================================================
Generation complete
============================================================
Created       : 100,000
Time          : 0.54 seconds
Average speed : 185,432 strings/sec
TXT file      : /path/to/passwords.txt

Creating ZIP...

ZIP created successfully.
ZIP file      : /path/to/passwords.zip
ZIP time      : 0.12 seconds

Done!
```

---

## Output Files

| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `passwords.txt` | Plain-text file with one generated string per line |
| `passwords.zip` | ZIP archive containing `passwords.txt`           |

Both files are created in the same directory where the script is run.

---

## Performance Notes

- Uses buffered writing (`1 MB` buffer) for efficient disk I/O.
- Generates passwords on the fly without loading everything into memory.
- Typical speed on modern hardware: **100,000 – 300,000+ strings per second** (depending on length and character set size).

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request.

---

## Disclaimer

This tool is intended **only for generating test data**.  
Do not use the generated strings as real passwords. Always use a proper password manager and strong, unique passwords for actual accounts.
