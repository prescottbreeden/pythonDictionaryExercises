# animals = [
# 	['dog','goes','woof'],
# 	['cat','goes','meow'],
# 	['bird','goes','tweet'],
# 	['mouse','goes','squeek'],
# 	['cow','goes','moo'],
# 	['frog','goes','croak'],
# 	['elephant','goes','toot'],
# 	['duck','say','quack'],
# 	['fish','go','blub'],
# 	['seal','goes','ow ow ow'],
# 	['fox','says','undefined...'],
# ]

# for animal in animals:
# 	print(f"{animal[0]} {animal[1]} {animal[2]}")


animals = {
	'dog':'woof',
	'cat':'meow',
	'bird':'tweet',
	'mouse':'squeek',
	'cow':'moo',
	'frog':'croak',
	'elephant':'toot',
	'duck':'quack',
	'fish':'blub',
	'seal':'ow ow ow',
	'fox':'undefined...',
}

for key in animals:
	print(f"{key} says {animals[key]}")





