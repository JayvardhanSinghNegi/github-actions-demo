import calculator

print("🔢 Calculator Outputs from GitHub Actions:")
print(f"2 + 3 = {calculator.add(2, 3)}")
print(f"10 - 4 = {calculator.subtract(10, 4)}")
print(f"5 * 6 = {calculator.multiply(5, 6)}")
print(f"20 / 5 = {calculator.divide(20, 5)}")

try:
    calculator.divide(1, 0)
except ValueError as e:
    print(f"❗ Handled divide by zero: {e}")

