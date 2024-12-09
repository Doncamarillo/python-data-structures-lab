#0 

def print_lakers_players():
    lakers_players = ['Lebron','AD','Austin Reaves']
    for player in lakers_players:
        print(player)

print_lakers_players()

#1

def manage_students():
    students = ['Lebron', 'Bronny', 'Lebron James Jr.']

    first_student = students[1]

    last_student = students [-1]

    return first_student,last_student

print (manage_students())

#2

def combine_food():

    food = ('pizza', 'chicken','lettuce')
    meal = ''
    for food in food: 
        meal += food + ' '
    return meal.strip() 

print (combine_food())

#3

def slice_foods():
    foods = ['fried rice', 'burger', 'orange chicken']
    last_two_foods = foods[-2:] 
    return last_two_foods

print(slice_foods())

#4

def hometown_info():
    hometown = {
        'city': 'Carson',
        'state': 'California',
        'population': 4549483
    }

    hometown_message = f"I was born in {hometown['city']}, {hometown['state']} - population of {hometown['population']}"

    return hometown_message
print(hometown_info())

#5 

home_town = {
    "city": "Los Angeles",
    "state": "California",
    "population": 540596
}

def list_home_town_items():
    home_town_items = []

    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    
    return home_town_items

print(list_home_town_items())

