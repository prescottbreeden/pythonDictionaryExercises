my_dict = {
	('Eli', 'cat'),
	('Anna', 'horse'),
	('Shane', 'dolphins'),
	('Oscar', 'llamas'),
	('Brendan', 'giraffe'),
	('Pariece', 'spider'),
	('Amy', 'ticks')
	}

for items in my_dict:
	print(f"{items[0]} loves {items[1]}")


my_dict2 = (
	{'Eli':'cat'},
	{'Anna':'horse'},
	{'Shane':'dolphins'},
	{'Oscar':'llamas'},
	{'Brendan':'giraffe'},
	{'Pariece':'spider'},
	{'Amy':'ticks'},
	)

for items in my_dict2:
	for people, values in items.items():
		print(people, values)


my_dict3 = [
	{'first_name':'Eli','animal':'cat'},
	{'first_name':'Anna','animal':'horse'},
	{'first_name':'Shane','animal':'dolphins'},
	{'first_name':'Oscar','animal':'llamas'},
	{'first_name':'Brendan','animal':'giraffe'},
	{'first_name':'Pariece','animal':'spider'},
	{'first_name':'Amy','animal':'ticks'},
	]

for items in my_dict3:
	print(f"{items['first_name']} fucking loves {items['animal']}")