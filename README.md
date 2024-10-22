# UniConvert

UniConvert is a simple command-line tool for converting between different units of measurement. It supports conversions for temperature, length, and weight.

## Features

- Temperature conversions: Celsius to Fahrenheit and vice versa
- Length conversions: meters to feet, kilometers to miles, and vice versa
- Weight conversions: kilograms to pounds and vice versa
- Easily scalable: adding new units is very simple

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/isakfiks/uniconvert.git
   ```

2. Navigate to the project directory:
   ```
   cd uniconvert
   ```

3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```


## Usage

Run the script from the command line with the following syntax:

```
python uniconvert.py <value> <from_unit> <to_unit>
```

Examples:

- Convert 32 Fahrenheit to Celsius:
  ```
  python uniconvert.py 32 f c
  ```

- Convert 10 meters to feet:
  ```
  python uniconvert.py 10 m ft
  ```

- Convert 5 kilograms to pounds:
  ```
  python uniconvert.py 5 kg lb
  ```

## Supported Units

- Temperature: c (Celsius), f (Fahrenheit)
- Length: m (meters), ft (feet), km (kilometers), mi (miles)
- Weight: kg (kilograms), lb (pounds)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
