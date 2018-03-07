users_dict = {
 'Students': [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

# .items()

for user in users_dict:
	for person in users_dict[user]:
		print(f"{person['first_name']} {person['last_name']}")

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

for user in users_dict:
  count = 1
  print(user)
  for person in users_dict[user]:
    x = len(person['first_name']+person['last_name'])
    print(f"{count} - {person['first_name']} {person['last_name']} - {x}")
    count += 1