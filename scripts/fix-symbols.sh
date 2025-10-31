# Remove extraneous characters (e.g. `§`,`^`,`*`,`¥`) and multi-tabs from the input

cat $1 | sed "s/§//g" | sed "s/\^//g" | sed "s/\xc2\xa5//g" | sed "s/\*//g" | sed "s/ \t/\t/g"
