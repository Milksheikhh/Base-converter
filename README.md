# Base Conversion Tool

This is a Python script that allows users to convert numbers between different bases: binary, decimal, hexadecimal, and octal.

## Features

- Convert from binary to decimal, octal, and hexadecimal
- Convert from decimal to binary, octal, and hexadecimal
- Convert from octal to decimal, binary, and hexadecimal
- Convert from hexadecimal to decimal, binary, and octal
- User-friendly command line interaction
- Validates user input and handles errors

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/S1lenc3XD/Base-converter.git
    cd base-conversion-tool
    ```

## Usage

1. Run the script:
    ```sh
    python base_conversion_tool.py
    ```

2. Follow the on-screen prompts to select the base you want to convert from and enter the number. The script will display the converted values in the other bases.

## Example

```sh
$ python base_conversion_tool.py
Would you like to convert from binary, decimal, hexadecimal or octal? binary
Please enter your binary number: 1010

Your binary number in:
decimal - 10
octal - 0o12
hexadecimal - 0xa

Would you like to run the program again? yes

Would you like to convert from binary, decimal, hexadecimal or octal? decimal
Please enter your decimal number: 15

Your decimal number in:
binary - 0b1111
octal - 0o17
hexadecimal - 0xf

Would you like to run the program again? no
