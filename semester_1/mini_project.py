input_planet = input("Which planet do you want to know your age on? Options: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto ")
input_age = input("How old are you? ")

num_earth_days = float(input_age) * 365


conversion_to_planet_factors = {"Mercury": 87.97, "Venus": 225, "Mars": 687 , "Jupiter": 4380, 
                                "Saturn": 10585, "Uranus": 30660, "Neptune": 60225, "Pluto": 90520}


print("You are " + str(round(num_earth_days / conversion_to_planet_factors[input_planet], 2)) + " years old on " + input_planet + ".")
