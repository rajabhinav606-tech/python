#!/usr/bin/env python3
"""Replace the nth digit of an integer.

Usage examples:
  python replace_nth_digit.py --number 1545 --n 2 --digit 9    # replaces 2nd digit from right
  python replace_nth_digit.py --number -1234 --n 1 --digit 7 --side left
  python replace_nth_digit.py --test
"""
import argparse
import sys


def replace_nth_digit(number: int, n: int, new_digit: int, from_left: bool = False) -> int:
    s = str(abs(number))
    if new_digit < 0 or new_digit > 9:
        raise ValueError("new_digit must be between 0 and 9")
    if n <= 0:
        raise ValueError("n must be a positive integer (1-based)")

    if from_left:
        idx = n - 1
    else:
        idx = len(s) - n

    if idx < 0 or idx >= len(s):
        raise IndexError("n is out of range for the given number")

    s = s[:idx] + str(new_digit) + s[idx + 1 :]
    result = int(s)
    return -result if number < 0 else result


def _run_tests():
    cases = [
        (1545, 1, 9, False, 1549),  # replace 1st from right -> last digit
        (1545, 2, 9, False, 1595),
        (1545, 4, 0, False, 545),
        (12345, 2, 0, True, 10345),  # 2nd from left
        (-9876, 1, 1, False, -9871),
    ]
    for num, n, d, left, expected in cases:
        try:
            out = replace_nth_digit(num, n, d, from_left=left)
        except Exception as e:
            print(f"FAIL {num=!r} {n=} {d=} {left=}: raised {e}")
            return 1
        if out != expected:
            print(f"FAIL {num=} {n=} {d=} {left=}: got {out}, expected {expected}")
            return 1
    print("All tests passed")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Replace the nth digit of an integer")
    p.add_argument("--number", type=int, help="The integer to modify")
    p.add_argument("--n", type=int, help="1-based position of digit to replace")
    p.add_argument("--digit", type=int, help="Replacement digit (0-9)")
    p.add_argument("--side", choices=("left", "right"), default="right",
                   help="Count from 'left' (most significant) or 'right' (least significant). Default: right")
    p.add_argument("--test", action="store_true", help="Run built-in tests")

    args = p.parse_args(argv)
    if args.test:
        return _run_tests()

    if args.number is None or args.n is None or args.digit is None:
        print("Interactive mode (press Enter to accept):")
        try:
            number = int(input("Number: ").strip())
            n = int(input("n (1-based): ").strip())
            digit = int(input("Replacement digit (0-9): ").strip())
            side = input("Side (left/right) [right]: ").strip() or "right"
        except Exception as e:
            print("Invalid input:", e)
            return 1
    else:
        number = args.number
        n = args.n
        digit = args.digit
        side = args.side

    try:
        out = replace_nth_digit(number, n, digit, from_left=(side == "left"))
    except Exception as e:
        print("Error:", e)
        return 1

    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
