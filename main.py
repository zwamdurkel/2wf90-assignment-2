import asn1tools as asn
import json

from method.addField import addField            # ✅(THOMAS) - FINNEAN # CORRECT
from method.addPoly import addPoly              # ✅ ALOYS # CORRECT
from method.addTable import addTable            # ✅ THOMAS # CORRECT
from method.displayField import displayField    # ✅ FINNEAN # CORRECT
from method.displayPoly import displayPoly      # ✅ FINNEAN # CORRECT
from method.divisionField import divisionField  # ✅ (FINNEAN) - ALOYS # CORRECT (maybe)
from method.equalsField import equalsField      # ✅ FINNEAN # CORRECT
from method.equalsPolyMod import equalsPolyMod  # ✅ FINNEAN # CORRECT
from method.euclidPoly import euclidPoly        # ✅ FINNEAN # CORRECT
from method.findIrred import findIrred          # THOMAS
from method.findPrim import findPrim    	    # THOMAS
from method.inverseField import inverseField    # ✅ FINNEAN # CORRECT
from method.irreducible import irreducible      # THOMAS
from method.longDivPoly import longDivPoly      # ✅ FINNEAN # CORRECT
from method.multiplyField import multiplyField  # ✅ FINNEAN # CORRECT
from method.multiplyPoly import multiplyPoly    # ✅ ALOYS # CORRECT
from method.multTable import multTable          # ✅ THOMAS # CORRECT
from method.primitive import primitive          # ✅ ALOYS # CORRECT
from method.subtractField import subtractField  # ✅ FINNEAN # CORRECT
from method.subtractPoly import subtractPoly    # ✅ ALOYS # CORRECT

# Below code should behave like a black-box.
# That means that by clicking RUN (and, perhaps, changing the location of the exercise file), your output file should be generated.

base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'input.ops'

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

    if operation == 'add-field':
        p['answer'], p['answer-poly'] = addField(
            p['mod'], p['mod-poly'], p['a'], p['b'])

    if operation == 'add-poly':
        p['answer'], p['answer-poly'] = addPoly(
            p['mod'], p['f'], p['g'])

    if operation == 'add-table':
        p['answer'], p['answer-poly'] = addTable(
            p['mod'], p['mod-poly'])

    if operation == 'display-field':
        p['answer'], p['answer-poly'] = displayField(
            p['mod'], p['mod-poly'], p['a'])

    if operation == 'display-poly':
        p['answer'] = displayPoly(
            p['mod'], p['f'])

    if operation == 'division-field':
        p['answer'], p['answer-poly'] = divisionField(
            p['mod'], p['mod-poly'], p['a'], p['b'])

    if operation == 'equals-field':
        p['answer'] = equalsField(
            p['mod'], p['mod-poly'], p['a'], p['b'])

    if operation == 'equals-poly-mod':
        p['answer'] = equalsPolyMod(
            p['mod'], p['f'], p['g'], p['h'])

    if operation == 'euclid-poly':
        p['answ-a'], p['answ-b'], p['answ-d'], p['answ-a-poly'], p['answ-b-poly'], p['answ-d-poly'] = euclidPoly(
            p['mod'], p['f'], p['g'])

    if operation == 'find-irred':
        p['answer'], p['answer-poly'] = findIrred(
            p['mod'], p['deg'])

    if operation == 'find-prim':
        p['answer'], p['answer-poly'] = findPrim(
            p['mod'], p['mod-poly'])

    if operation == 'inverse-field':
        p['answer'], p['answer-poly'] = inverseField(
            p['mod'], p['mod-poly'], p['a'])

    if operation == 'irreducible':
        p['answer'] = irreducible(
            p['mod'], p['f'])

    if operation == 'long-div-poly':
        p['answ-q'], p['answ-r'], p['answ-q-poly'], p['answ-r-poly'] = longDivPoly(
            p['mod'], p['f'], p['g'])

    if operation == 'multiply-field':
        p['answer'], p['answer-poly'] = multiplyField(
            p['mod'], p['mod-poly'], p['a'], p['b'])

    if operation == 'multiply-poly':
        p['answer'], p['answer-poly'] = multiplyPoly(
            p['mod'], p['f'], p['g'])

    if operation == 'mult-table':
        p['answer'], p['answer-poly'] = multTable(
            p['mod'], p['mod-poly'])

    if operation == 'primitive':
        p['answer'] = primitive(
            p['mod'], p['mod-poly'], p['a'])

    if operation == 'subtract-field':
        p['answer'], p['answer-poly'] = subtractField(
            p['mod'], p['mod-poly'], p['a'], p['b'])

    if operation == 'subtract-poly':
        p['answer'], p['answer-poly'] = subtractPoly(
            p['mod'], p['f'], p['g'])

    # Save answer
    my_answers['exercises'].append({operation: p})

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+")  # write to binary file
my_file.write(json.dumps(my_answers).encode())  # add encoded exercise list
my_file.close()
