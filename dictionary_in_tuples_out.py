my_dict = {
	"Speros": "(555) 555-5555",
	"Michael": "(999) 999-9999",
	"Jay": "(777) 777-7777"
}

def dictionary_to_tuples(dict):
	list_of_poeple = []
	for person in dict:
		person_data = (person, dict[person])
		list_of_poeple.append(person_data)
	print(list_of_poeple)

dictionary_to_tuples(my_dict)