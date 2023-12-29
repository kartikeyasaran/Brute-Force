# Bruteforce Tool

A simple password bruteforce tool implemented in Python using the PyAutoGUI library.

## Disclaimer

This tool is intended for educational purposes only. Unauthorized use is strictly prohibited. The developers are not responsible for any misuse or damage caused by this tool.

## Features

- Brute forces passwords using PyAutoGUI library
- Requires a wordlist file for password guessing

## Prerequisites

- Python 3.x
- PyAutoGUI library

## Usage

1. Install the required libraries:

    ```bash
    pip install pyautogui
    ```

2. Run the script:

    ```bash
    python bruteforce.py -w wordlist.txt
    ```

    Replace `wordlist.txt` with the path to your wordlist file.

## Options

- `-w, --wordlist`: Path to the wordlist file (required)

## Contributing

If you'd like to contribute to this project, please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
