# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin="malwmrllpllallalwgpdpaaa"
bInsulin="fvnqhlcgshlvealylvcgergffytpkt"
aInsulin="giveqcctsicslyqlenycn"
cInsulin="rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin
print(insulin)

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")

# Printing to console using concatenated strings inside the print function (one-liner):

print("The sequence of human insulin, chain a: " + aInsulin)

print("The sequence of human insulin, chain a:", aInsulin)
