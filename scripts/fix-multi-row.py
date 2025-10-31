# fix-multi-row.py
# Usage: python fix-multi-row.py data.tsv

import sys

filename = sys.argv[1]

with open(filename) as fp:
	lines = [line.split('\t') for line in fp.readlines()]

fixed = [lines[0].copy()]

for i in range(1, len(lines), 2):
	x = lines[i]
	y = lines[i+1]
	z = []

	for j in range(len(lines[i])):
		if x[j] == '':
			z.append(y[j])
		elif y[j] == '':
			z.append(x[j])
		else:
			z.append(x[j].strip() + ' ' + y[j].strip())

	fixed.append(z.copy())

with open(filename + '.new.tsv', 'w') as fp:
	fp.write('\n'.join(['\t'.join(line) for line in fixed]))
