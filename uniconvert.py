import argparse
import sys

# Conversion factors and functions
TEMP_CONVERSIONS = {
    "c_to_f": lambda c: c * 9/5 + 32,
    "f_to_c": lambda f: (f - 32) * 5/9,
}

LENGTH_CONVERSIONS = {
    "m_to_ft": 3.28084,
    "m_to_km": 0.001,
    "km_to_m": 1000,
    "ft_to_m": 0.3048,
    "km_to_mi": 0.621371,
    "mi_to_km": 1.60934,
}

WEIGHT_CONVERSIONS = {
    "kg_to_lb": 2.20462,
    "lb_to_kg": 0.453592,
}

def convert_temp(value, from_unit, to_unit):
    # Temperature needs custom handling
    if f"{from_unit}_to_{to_unit}" in TEMP_CONVERSIONS:
        return TEMP_CONVERSIONS[f"{from_unit}_to_{to_unit}"](value)
    else:
        return value

def convert_unit(value, from_unit, to_unit, conversion_dict):
    # Generic conversion
    if from_unit == to_unit:
        return value
    elif f"{from_unit}_to_{to_unit}" in conversion_dict:
        return value * conversion_dict[f"{from_unit}_to_{to_unit}"]
    elif f"{to_unit}_to_{from_unit}" in conversion_dict:
        return value / conversion_dict[f"{to_unit}_to_{from_unit}"]
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is currently not supported")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert between different units of measurement.")
    parser.add_argument("value", type=float, help="The value to convert")
    parser.add_argument("from_unit", help="The unit to convert from")
    parser.add_argument("to_unit", help="The unit to convert to")
    args = parser.parse_args()

    # Determine the type of conversion
    if args.from_unit in ["c", "f"] and args.to_unit in ["c", "f"]:
        result = convert_temp(args.value, args.from_unit, args.to_unit)
    elif args.from_unit in ["m", "ft", "km", "mi"] and args.to_unit in ["m", "ft", "km", "mi"]:
        result = convert_unit(args.value, args.from_unit, args.to_unit, LENGTH_CONVERSIONS)
    elif args.from_unit in ["kg", "lb"] and args.to_unit in ["kg", "lb"]:
        result = convert_unit(args.value, args.from_unit, args.to_unit, WEIGHT_CONVERSIONS)
    else:
        print(f"Conversion from {args.from_unit} to {args.to_unit} not supported")
        sys.exit(1)

    # Show the result
    print(f"{args.value} {args.from_unit} is equal to {result:.2f} {args.to_unit}")

if __name__ == "__main__":
    main()
