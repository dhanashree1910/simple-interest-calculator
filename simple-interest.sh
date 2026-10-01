#!/bin/bash
# Simple Interest Calculator Shell Script

# Author: Dhanashree Jagtap
# Input:
# p: Principal amount
# r: Annual rate of interest
# t: Time period in years

# Output:
# Simple Interest = (p * r * t) / 100

echo "=== Simple Interest Calculator ==="
echo -n "Enter Principal Amount (P): "
read p
echo -n "Enter Annual Rate of Interest (R in %): "
read r
echo -n "Enter Time Period in Years (T): "
read t

# Calculate Simple Interest
s=$(echo "scale=2; ($p * $r * $t) / 100" | bc 2>/dev/null || expr $p \* $r \* $t / 100)

echo "---------------------------------"
echo "Simple Interest: $s"
