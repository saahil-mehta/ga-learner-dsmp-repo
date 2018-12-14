# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

class_1

class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

class_2

new_class=class_1+class_2

new_class

new_class.append('Peter Warden')

new_class

new_class.remove("Carla Gentry")

new_class


# --------------
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}

courses

#[] for calling dict values 
#courses["Math"]

total=sum(courses.values())

total

percentage=(total/500)*100

percentage


# --------------
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}

mathematics

topper=max(mathematics, key=mathematics.get)

topper


# --------------
topper = 'andrew ng'

topper.split(" ")

first_name=topper.split()[0]

last_name=topper.split()[1]

first_name,last_name

full_name=last_name+" "+first_name

full_name

certificate_name=full_name.upper()

certificate_name


