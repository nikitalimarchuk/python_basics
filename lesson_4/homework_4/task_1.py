"""
This module could be used from console.
Please use next command to get salary of employee:
python task_1.py -name John -rate 10 -hours 168 -prize 1500
"""


import argparse
from decimal import Decimal

ap = argparse.ArgumentParser()
ap.add_argument("-name", "--coperand", required=True)
ap.add_argument("-rate", "--foperand", required=True)
ap.add_argument("-hours", "--soperand", required=True)
ap.add_argument("-prize", "--voperand", required=True)
args = vars(ap.parse_args())
name, hours, rate, prize = args.values()

print(f"{name} salary is: {Decimal(hours) * Decimal(rate) + Decimal(prize)}")
