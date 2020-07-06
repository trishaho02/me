TODO: Reflect on what you learned this week and what is still unclear.

ex1
- need help with the id section 
- parse - looked up parts for parse json 
- password, ID and postcode 

- word pyramid: how to write the code out 
- pokemon one: where is the request library 

results = '{"lastName": hoogmoed, "password": jokers, "postcodePlusID": }'
    try: and debug it
    results_dict = json.loads(results)
    print(results_dict['lastName'])
    print(results_dict['password'])
    print(results_dict['postcodePlusID'])

for pokedex:
# low to high of the pokemons 
    # begin with the lowest then one above that 
    # sort pokedex at the end in ascending order

    # for low and high pokemons 
    # has victreebel, blastois, golduck, ivysaur 

notes from: 
-

attempt:
pokemons = [] # to array the pokemons - use range and list out items 
    for x in range(low, high):
    url = template.format(id=5)
    r = requests.get(url)
    if r.status_code is 200:
        the_json = json.loads(r.text)
        pokemons.append(the_json)
    
    for y in pokemons:
        height = y["height"]
        if height > tallest_pokemon:
            tallest_pokemon = height 
            first_name = y["name"]
            first_weight = y["weight"]
            first_height = y["height"]

