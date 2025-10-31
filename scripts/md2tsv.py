# md2tsv.py
# Usage: python md2tsv.py ocr-output.md

import re
import csv
import sys

md_file = sys.argv[1]
identifier = md_file.split('/')[-1]

with open(md_file) as md_fp:
	md_content = md_fp.read()

md_tables = md_content.split('\n\n')

def extract_header(row):
	cells = row.split('|')
	header = [cell.strip().replace('<br>', ' ').replace('<br/>', ' ') for cell in cells[1:-1]]

	return header

def extract_values(row):
	cells = row.split('|')
	values = [re.sub(r'(\d)\s+(\d)', r'\1\2', cell.strip().replace('<br>', ' ')) for cell in cells[1:-1]]

	return values

def parse_table(md_table):
	table = []
	rows = md_table.split('\n')

	# Extract header
	header = extract_header(rows[0])
	if header[0].startswith('WHO Region') or header[0].startswith('Reporting Country'):
		table = []

	table.append(header)

	# Extract values from rows
	for row in rows[2:]:
		values = extract_values(row)
		table.append(values)

	return table

def write_tsv(filename, table):
	with open(filename, "w") as tsv_fp:
		writer = csv.writer(tsv_fp, delimiter='\t', lineterminator='\n')
		for row in table:
			writer.writerow(row)

file_idx = 0
for md_table in md_tables:
	table = parse_table(md_table)
	
	# Only write tables which report new number of cases and deaths
	if table[0][0].startswith('WHO Region') or table[0][0].startswith('Reporting Country'):
		file_idx += 1
		filename = '%s-%s.tsv' % (identifier, file_idx)
		write_tsv(filename, table)
