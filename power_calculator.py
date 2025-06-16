import math 

def calculate_power(V, I, PF):
  if PF<0 or PF>1:
    return "Power Factor must be between 0 and 1."
  else:
    P = 1.73 * V * I * PF               #Real Power
    angle = math.acos(PF)
    Q = 1.73 * V * I * math.sin(angle)  #Reactive Power
    S = 1.73 * V * I                    #Apparent Power
    return f"""Real Power is: {P:.2f} Watts \nand Reactive Power is: {Q:.2f} VAR \nand Apparent Power is: {S:.2f} VA"""

V = float(input("Enter Voltage (V): "))
I = float(input("Enter Current (A): "))
PF = float(input("Enter Power Factor (PF): "))
print(calculate_power(V, I, PF))
