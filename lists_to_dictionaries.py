names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
	for name in names:
		new_dict = zip(names, favorite_animal)
		result = set(new_dict)
	print(result)
	return result

make_dict(names, favorite_animal)
