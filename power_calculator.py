def calculate_power(V, I, PF):
  if PF<0 or PF>1:
    return "Power Factor must be between 0 and 1."
  else:
    P = 1.73 * V * I * PF
    return f"Rated Power is: {P} watts"

V = float(input("Enter Voltage (V): "))
I = float(input("Enter Current (A): "))
PF = float(input("Enter Power Factor (PF): "))
print(calculate_power(V, I, PF))
