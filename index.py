from flask import Flask, jsonify, request
import sys


#Init 
app = Flask(__name__)


recipes = [
    {
      "name": "scrambledEggs",
      "ingredients": [
        "1 tsp oil",
        "2 eggs",
        "salt"
      ],
      "instructions": [
        "Beat eggs with salt",
        "Heat oil in pan",
        "Add eggs to pan when hot",
        "Gather eggs into curds, remove when cooked",
        "Salt to taste and enjoy"
      ]
    },
    {
      "name": "garlicPasta",
      "ingredients": [
        "500mL water",
        "100g spaghetti",
        "25mL olive oil",
        "4 cloves garlic",
        "Salt"
      ],
      "instructions": [
        "Heat garlic in olive oil",
        "Boil water in pot",
        "Add pasta to boiling water",
        "Remove pasta from water and mix with garlic olive oil",
        "Salt to taste and enjoy"
      ]
    },
    {
      "name": "chai",
      "ingredients": [
        "400mL water",
        "100mL milk",
        "5g chai masala",
        "2 tea bags or 20 g loose tea leaves"
      ],
      "instructions": [
        "Heat water until 80 C",
        "Add milk, heat until 80 C",
        "Add tea leaves/tea bags, chai masala; mix and steep for 3-4 minutes",
        "Remove mixture from heat; strain and enjoy"
      ]
    },
    {
      "name": "butteredBagel", 
      "ingredients": [
          "1 bagel", 
          "butter"
      ], 
      "instructions": [
        "cut the bagel", 
        "spread butter on bagel"
      ] 
    } 
  ]

# Db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# @app.route('/recipes', methods=['GET', 'POST', 'PUT'])
# def food_recipes():
#   if request.method == 'POST':
#     food_name = ''
#     reply = {}
#     recipeN = []
#     error_message = {"error": "Recipe already exists"}
#     new_food = request.get_json(silent= True)
    
#     for i in recipes:
#         for j in i:
#             if j == 'name':
#                 recipeN.append(i[j])
#     reply['recipeNames'] = recipeN

#     for x, y in new_food.items():
#         if x == 'name': 
#             food_name += y

#     if food_name in recipeN:
#       return error_message
    
#     else: 
#       recipes.append(request.get_json())
#       return '', 204

#   elif request.method == 'PUT':
#     new_recip = request.get_json(silent= True)
#     error_message = {"error": "Recipe does not exists"}
#     print(new_recip, file=sys.stderr)

#     for i in recipes:
#       if new_recip['name'] in i.values():
#           print(new_recip, file=sys.stderr)
#           return i.update(update_food)
#       elif update_food['name'] not in i.values():
#           print(i, file=sys.stderr)
#           return error_message
      

    
#   else: 
#     recipeNames = []
#     for food in recipes:
#         for i in food:
#             if i == 'name':
#                 recipeNames.append(food[i])
#     return jsonify({"recipeNames": recipeNames}), 200
    


# @app.route('/recipes', methods=['POST'])
# def add_recipes():

@app.route('/recipes', methods=['GET'])
def get_recipes():
  recipeNames = []
  for food in recipes:
      for i in food:
          if i == 'name':
              recipeNames.append(food[i])
  return jsonify({"recipeNames": recipeNames}), 200

@app.route('/recipes', methods=['POST'])
def post_recipes():
  food_name = ''
  reply = {}
  recipeN = []
  error_message = {"error": "Recipe already exists"}
  new_food = request.get_json(silent= True)
  
  for i in recipes:
      for j in i:
          if j == 'name':
              recipeN.append(i[j])
  reply['recipeNames'] = recipeN

  for x, y in new_food.items():
      if x == 'name': 
          food_name += y

  if food_name in recipeN:
    return error_message
  
  else: 
    recipes.append(request.get_json())
    return '', 204

@app.route('/recipes', methods=['PUT'])
def put_recipe():
    new_recip = request.get_json(silent= True)
    error_message = {"error": "Recipe does not exists"}

    for i in recipes:
      print(i, file=sys.stderr)
      if new_recip['name'] in i.values():
          i.update(request.get_json())
          return '', 204
    return error_message


@app.route('/recipes/details/<food>', methods=['GET'])
def get_specific_food(food):
  numSteps = 0
  details = {}
  for i in recipes:
      if i['name'] == food:
      #    ingredients.append(i['ingredients'])
          details['ingredients'] = i['ingredients']
          numSteps += len(i['instructions'])
  details['numSteps'] = numSteps
  return jsonify({"details": details}), 200











# @app.route('/incomes', methods=['POST'])
# def add_income():
#   incomes.append(request.get_json())
#   return '', 204


if __name__ == "__main__":
	app.run(debug=True)