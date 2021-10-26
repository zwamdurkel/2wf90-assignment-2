import asn1tools as asn
import json

from method.addField import addField
from method.addPoly import addPoly  # ALOYS # CORRECT
from method.addTable import addTable
from method.displayField import displayField
from method.displayPoly import displayPoly
from method.divisionField import divisionField
from method.equalsField import equalsField
from method.equalsPolyMod import equalsPolyMod
from method.euclidPoly import euclidPoly
from method.findIrred import findIrred
from method.findPrim import findPrim
from method.inverseField import inverseField
from method.irreducible import irreducible
from method.longDivPoly import longDivPoly
from method.multiplyField import multiplyField
from method.multiplyPoly import multiplyPoly
from method.multTable import multTable
from method.primitive import primitive
from method.subtractField import subtractField
from method.subtractPoly import subtractPoly  # ALOYS # CORRECT

### STUDENT PERSPECTIVE (example) ###

# Below code should behave like a black-box.
# That means that by clicking RUN (and, perhaps, changing the location of the exercise file), your output file should be generated.

base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'custom.ops'

# Compile specification
spec = asn.compile_files(ops_loc, codec="jer")

# Read exercise list
exercise_file = open(exs_loc, 'rb')  # open binary file
file_data = exercise_file.read()  # read byte array
# decode after specification
my_exercises = spec.decode('Exercises', file_data)
exercise_file.close()  # close file

# Create answer JSON
my_answers = {'exercises': []}

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0]  # get operation type
    p = exercise[1]  # get parameters

    if operation == 'add-poly':
        p['answer'], p['answer-poly'] = addPoly(
            p['mod'], p['f'], p['g'])

    if operation == 'display-poly':
        p['answer'] = displayPoly(
            p['mod'], p['f'])

    if operation == 'subtract-poly':
        p['answer'], p['answer-poly'] = subtractPoly(
            p['mod'], p['f'], p['g'])

    # Save answer
    my_answers['exercises'].append({operation: p})

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+")  # write to binary file
my_file.write(json.dumps(my_answers).encode())  # add encoded exercise list
my_file.close()
