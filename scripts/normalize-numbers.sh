# Normalize numbers in a given text file
# e.g., 1 234 567 is converted to 1234567

cat $1 | sed -r 's:([0-9]+) ([0-9]+) ([0-9]+):\1\2\3:g' | sed  -r 's:([0-9]+) ([0-9]+):\1\2:g'
