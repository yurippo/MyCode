statesOfAmerica = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut",
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York",
"North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
"Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
"Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas","West Virginia",
"Nevada", "Nebraska", "Colorado","North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
"Wyoming", "Utah", "Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]

##To change data inside of my python list
statesOfAmerica[1] = "Pencilvania"

print(statesOfAmerica[1])

##To add an item to the end of the list

statesOfAmerica.append("Angelaland")

##Use extend to add a bunch of items to the list

statesOfAmerica.extend(["Yuriland","Jack Bauer Land"])

print(statesOfAmerica)
