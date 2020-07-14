planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptuno"])
planet_list.append("Pluto")
my_slice = slice(2)
rocky_planets = planet_list[my_slice]
print(f"rocky={rocky_planets}")
planet_list.remove("Pluto")
print(planet_list)
