import sys

print("This program calculates the kinetic energy of a moving object.")

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python kinetic_energy.py <mass_in_kg> <speed_in_mps>")
    sys.exit(1)

mass = float(sys.argv[1])
speed = float(sys.argv[2])

kinetic_energy = 0.5 * mass * speed ** 2

print("The object has", kinetic_energy, "joules of energy.")

