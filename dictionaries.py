# similar to a hash

audiSport = {}

audiSport["Sedan"] = "RS4"
audiSport["Coupe"] = "RS5"
audiSport["Shooting Brake"] = "RS7"
audiSport["Exotic"] = "R8 V10+"
audiSport["Estate"] = "RS6 Avant"

print(audiSport["Exotic"])
# to make it fail gracefully when a nonexistent key is referenced

print(audiSport.get('Front-wheel-drive'))

for type in audiSport: 
	print (type + ': ' + audiSport[type] )