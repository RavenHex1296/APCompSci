input_age = input("How old are you? ")

num_earth_days = float(input_age) * 365


conversion_to_planet_factors = {"Mercury": 87.97, "Venus": 225, "Mars": 687 , "Jupiter": 4380, 
                                "Saturn": 10585, "Uranus": 30660, "Neptune": 60225, "Pluto": 90520}


for planet in conversion_to_planet_factors:
    print("You are " + str(round(num_earth_days / conversion_to_planet_factors[planet], 2)) + " years old on " + planet + ".")
