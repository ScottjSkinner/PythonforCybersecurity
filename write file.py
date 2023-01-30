name = input("What is your name  :")

color = input("What is your favorite color  :")

pet = input("What was your first pet's name  :")

mmn = input("What is your mother's maiden name  :")

school = input("What elementary school did you attend  :")

hack_me = open("hackme.txt", "w")
hack_me.write(name)
hack_me.write("\n")
hack_me.write(color)
hack_me.write("\n")
hack_me.write(pet)
hack_me.write("\n")
hack_me.write(mmn)
hack_me.write("\n")
hack_me.write(school)

hack_me.close()
