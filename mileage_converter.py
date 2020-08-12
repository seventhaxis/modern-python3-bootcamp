print("How many miles did you cycle today?"")

miles = input()
kms = float(miles) * 1.60934
result = str(round(kms, 2))

print(f"This is equal to {result} kilometers.")
