# Remove references to figures and tables in the text

cat $1 | \
	sed -r 's/ \([Ff]igure [0-9]+[A|B], [Tt]able [0-9]+\)//g' | \
	sed -r 's/ \([Ff]igure [0-9]+, [Tt]able [0-9]+\)//g' | \
	sed -r 's/ \([Ff]igure [0-9]+, [Tt]able-[0-9]+\)//g' | \
	sed -r 's/ \([Tt]able [0-9]+, [Tt]able [0-9]+\)//g' | \
	sed -r 's/ \([Tt]able [0-9]+, [Tt]able [0-9]+,//g' | \
	sed -r 's/ \([Tt]able[s]? [0-9]+ and [0-9]+\)//g' | \
	sed -r 's/ \([Ff]igure [0-9]+\)//g' | \
	sed -r 's/ \([Tt]able [0-9]+\)//g' | \
	sed -r 's/ [Ff]igure [0-9]+\)//g'
