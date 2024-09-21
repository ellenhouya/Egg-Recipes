from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)


meals= [
    {
      "idMeal": "01",
      "mealName": "Blini Pancakes",
      "category": ["Side", "Dessert"],
      "area": "Russian",
      "instructions": "In a large bowl, whisk together 1/2 cup buckwheat flour, 2/3 cup all-purpose flour, 1/2 teaspoon salt, and 1 teaspoon yeast.\r\n\r\nMake a well in the center and pour in 1 cup warm milk, whisking until the batter is smooth.\r\n\r\nCover the bowl and let the batter rise until doubled, about 1 hour.\r\n\r\nEnrich and Rest the Batter\r\nStir 2 tablespoons melted butter and 1 egg yolk into the batter.\r\n\r\nIn a separate bowl, whisk 1 egg white until stiff, but not dry.\r\n\r\nFold the whisked egg white into the batter.\r\n\r\nCover the bowl and let the batter stand 20 minutes.\r\n\r\nPan-Fry the Blini\r\nHeat butter in a large nonstick skillet over medium heat.\r\n\r\nDrop quarter-sized dollops of batter into the pan, being careful not to overcrowd the pan. Cook for about 1 minute or until bubbles form.\r\n\r\nTurn and cook for about 30 additional seconds.\r\n\r\nRemove the finished blini onto a plate and cover them with a clean kitchen towel to keep warm. Add more butter to the pan and repeat the frying process with the remaining batter.",
      "mealThumb": "https://www.themealdb.com/images/media/meals/0206h11699013358.jpg",
      "youtube": "https://www.youtube.com/embed/GsB8ZI5vREA",
      "ingredientsMeasuers": {
        "Buckwheat": "1/2 cup",
        "Flour": "2/3 Cup",
        "Salt": "1/2 tsp",
        "Yeast": "1 tsp",
        "Milk": "1 cup",
        "Butter": "2 tbs",
        "Egg": "1 Seperated"
      },
      "rating": 5,

      "nutritionFacts": {
          "Calories": 96,
          "Fat":"20g",
          "Saturated Fat":"2.9g",
          "Trans Fat" : "0.2g",
           "Polyunsaturated Fat": "0.5g",
           "Monounsaturated Fat":"1.5g",
           "Cholesterol":"66mg",
           "Salt":"0.3g",
      },
      "calLevel": "Low"
    },
    {
      "idMeal": "02",
      "mealName": "Apple Frangipan Tart",
      "category": ["Side", "Dessert"],
      "area": "British",
      "instructions": "Preheat the oven to 200C/180C Fan/Gas 6.\r\nPut the biscuits in a large re-sealable freezer bag and bash with a rolling pin into fine crumbs. Melt the butter in a small pan, then add the biscuit crumbs and stir until coated with butter. Tip into the tart tin and, using the back of a spoon, press over the base and sides of the tin to give an even layer. Chill in the fridge while you make the filling.\r\nCream together the butter and sugar until light and fluffy. You can do this in a food processor if you have one. Process for 2-3 minutes. Mix in the eggs, then add the ground almonds and almond extract and blend until well combined.\r\nPeel the apples, and cut thin slices of apple. Do this at the last minute to prevent the apple going brown. Arrange the slices over the biscuit base. Spread the frangipane filling evenly on top. Level the surface and sprinkle with the flaked almonds.\r\nBake for 20-25 minutes until golden-brown and set.\r\nRemove from the oven and leave to cool for 15 minutes. Remove the sides of the tin. An easy way to do this is to stand the tin on a can of beans and push down gently on the edges of the tin.\r\nTransfer the tart, with the tin base attached, to a serving plate. Serve warm with cream, crème fraiche or ice cream.",
      "mealThumb":"https://www.themealdb.com/images/media/meals/wxywrq1468235067.jpg",
      "youtube": "https://www.youtube.com/embed/kgL9CWUgAYU",
      "ingredientsMeasuers": {
        "digestive biscuits": "175g/6oz",
        "butter": "75g/3oz",
        "Bramley apples": "200g/7oz",
        "butter, softened": "75g/3oz",
        "caster sugar": "75g/3oz",
        "free-range eggs, beaten": "2",
        "ground almonds": "75g/3oz",
        "almond extract": "1 tsp",
        "flaked almonds": "50g/1¾oz",
      },
      "rating": 4,
      
       "nutritionFacts": {
          "Calories": 264,
          "Total Fat":" 13g",
          "Saturated Fat":"4g",
          "Trans Fat" : "0g",
          "Total Carbs": "43g",
          "Dietary Fiber":"3mg",
          "Total Sugars":" 22g",
      },
      "calLevel": "Medium"
    },
    
    {
      "idMeal": "03",
      "mealName": "Apple Crumble",
      "category": ["Side", "Dessert"],
      "area": "British",
      "instructions": "Heat oven to 190C/170C fan/gas 5. Tip the flour and sugar into a large bowl. Add the butter, then rub into the flour using your fingertips to make a light breadcrumb texture. Do not overwork it or the crumble will become heavy. Sprinkle the mixture evenly over a baking sheet and bake for 15 mins or until lightly coloured.\r\nMeanwhile, for the compote, peel, core and cut the apples into 2cm dice. Put the butter and sugar in a medium saucepan and melt together over a medium heat. Cook for 3 mins until the mixture turns to a light caramel. Stir in the apples and cook for 3 mins. Add the blackberries and cinnamon, and cook for 3 mins more. Cover, remove from the heat, then leave for 2-3 mins to continue cooking in the warmth of the pan.\r\nTo serve, spoon the warm fruit into an ovenproof gratin dish, top with the crumble mix, then reheat in the oven for 5-10 mins. Serve with vanilla ice cream.",
      "mealThumb": "https://www.themealdb.com/images/media/meals/xvsurr1511719182.jpg",
      "youtube": "https://www.youtube.com/embed/nnNObNyfUnE",
      "ingredientsMeasuers": {
        "Plain Flour": "120g",
        "Caster Sugar": "60g",
        "Butter": "60g",
        "Braeburn Apples": "300g",
        "Butter":"30g",  
        "Demerara Sugar": "30g",
        "Blackberrys": "120g",
        "Cinnamon": "¼ teaspoon",
        "Ice Cream": "to serve"
      },
      "rating": 4,

       "nutritionFacts": {
          "Calories": 190,
          "Total Fat":" 1.5g",
          "Cholesterol":"0g",
          "Sodium" : "0mg",
          "Total Carbohydrate": "44g",
          "Dietary Fiber":"5g",
          "Total Sugars":" 27g",
          "Protein":"3g",
      },
      "calLevel": "Moderate"
    },

    {
      "idMeal": "04",
      "mealName": "Boxty Breakfast",
      "category": ["Breakfast", "Side"],
      "area": "Irish",
     "instructions": "STEP 1\r\nBefore you start, put your oven on its lowest setting, ready to keep things warm. Peel the potatoes, grate 2 of them, then set aside. Cut the other 2 into large chunks, then boil for 10-15 mins or until tender. Meanwhile, squeeze as much of the liquid from the grated potatoes as you can using a clean tea towel. Mash the boiled potatoes, then mix with the grated potato, spring onions and flour.\r\n\r\nSTEP 2\r\nWhisk the egg white in a large bowl until it holds soft peaks. Fold in the buttermilk, then add the bicarbonate of soda. Fold into the potato mix.\r\n\r\nSTEP 3\r\nHeat a large non-stick frying pan over a medium heat, then add 1 tbsp butter and some of the oil. Drop 3-4 spoonfuls of the potato mixture into the pan, then gently cook for 3-5 mins on each side until golden and crusty. Keep warm on a plate in the oven while you cook the next batch, adding more butter and oil to the pan before you do so. You will get 16 crumpet-size boxty from the mix. Can be made the day ahead, drained on kitchen paper, then reheated in a low oven for 20 mins.\r\n\r\nSTEP 4\r\nHeat the grill to medium and put the tomatoes in a heavy-based pan. Add a good knob of butter and a little oil, then fry for about 5 mins until softened. Grill the bacon, then pile onto a plate and keep warm. Stack up the boxty, bacon and egg, and serve the tomatoes on the side.",
      "mealThumb": "https://www.themealdb.com/images/media/meals/naqyel1608588563.jpg",
      "youtube": "https://www.youtube.com/embed/80W0mCFDIP0",
      "ingredientsMeasuers": {
        "Potatoes": "4 large",
        "Spring Onions": "1 bunch",
        "Plain Flour": "100g",
        "Egg White": "1",
        "Milk":"150ml",  
        "Bicarbonate Of Soda": "1 tsp",
        "Butter": "3 tbs",
        "Vegetable Oil": "2 tbs",
        "Cherry Tomatoes": "6",
        "Bacon": "12",
        "Egg": "6"
      },
      "rating": 3,

      "nutritionFacts": {
          "Calories": 310,
          "Total Fat":" 19g",
          "Sodium" : "770mg",
          "Cholesterol":"80mg",
          "Vitamin C": "18mg",
          "Carbohydrates":"33g",
          "Fiber":" 1g",
          "Protein":"5g",
      },
      "calLevel": "High"
    },

    {
        "idMeal": "05",
        "mealName": "Bread Omelette",
        "category": ["Breakfast", "Lunch"],
        "area": "Irish",
        "instructions": "Two eggs is ideal for one sandwich. Country eggs taste really great in a bread omelette. But use whatever eggs you have on hand. Break the eggs in a bowl and set aside. Add in the salt and turmeric powder. I like to add turmeric powder to my omelette as it gives a nice bright yellow colour that's so good. It is not very traditional to add turmeric but I love it in my omelet. Add in the finely chopped onions, green chillies and coriander leaves. Add a little water. The water will lighten the batter and makes for really soft omelettes. Instead of water, one can use a tablespoon of milk too. Whisk everything with a fork for a few seconds. Set aside. Heat butter in a pan until hot. You can use oil instead of butter but I advise you to use butter as the flavour of butter cannot be beat. Add in the omelette mixture to the pan. Swirl the pan so the omelette mixture evenly spread and covers the width of the pan. Add two bread slices on top of the omelette. Milk bread, Brown bread, Whole Wheat anything will work well. Immediately flip the bread. A little bit of the egg mixture would stick to the bread. Sprinkle black pepper. Be lavish with black pepper. Freshly ground black pepper adds a nice aroma and flavour. Cook for 30 seconds on a medium flame. Now, flip the omelette along with the bread slices. Fold the omelette on the bread like the picture below. Watch the video if doubtful. Add half a teaspoon of butter so the bread can nicely toast and crisp up into a beautiful sandwich. Spread a little mayonnaise on one side of the omelette. This is not very traditional but mayonnaise gives a very nice and smooth mouthfeel to the sandwich. Fold the sandwich and cook the sides like the picture below. Remove the bread omelette sandwich from the pan and cut into four slices. Sprinkle a little coriander leaves and green chillies. Serve hot with tea.",
      "mealThumb": "https://www.themealdb.com/images/media/meals/hqaejl1695738653.jpg",
      "youtube": "https://www.youtube.com/embed/0ju2twft8V0",
      "ingredientsMeasuers": {
        "Bread": "2",
        "Egg": "2",
        "Salt": "0.5", 
      },
      "rating": 5,

      "nutritionFacts": {
          "Calories": 356,
          "Total Fat":" 16g",
          "Saturated Fat": "3.9g",
          "Polyunsaturated Fat ":"5.9g",
          "Monounsaturated Fat":"5.1g",
          "Cholesterol":"372mg",
          "Sodium" : "608mg",
          "Total Carbohydrates":" 33g",
      },
      "calLevel": "High"
    },

    {
        "idMeal": "06",
        "mealName": "Chivito uruguayo",
        "category": ["Breakfast", "Side"],
        "area": "Taiwanese",
        "instructions": "Crush the meat so that it is finite and we put it on a griddle to brown. Put the eggs, bacon and ham to fry.\r\nCut the bread in half, put the beef brisket, the fried eggs, the bacon, the ham, the mozzarella, the tomato and the lettuce. Cover with the other half of the bread and serve.",
        "mealThumb": "https://www.themealdb.com/images/media/meals/n7qnkb1630444129.jpg",
        "youtube": "https://www.youtube.com/embed/VTcRZANmFKM",
        "ingredientsMeasuers": {
        "Beef Brisket": "2",
        "Bread": "2",
        "Lettuce": "1", 
        "Tomato":"1",
        "Ham":"100g",
        "Mozzarella":"100g",
        "Bacon":"100g",
        "Egg":"1",
        "Onion":"1",
        "Pepper":"1",
      },
      "rating": 3,

       "nutritionFacts": {
          "Calories": 995,
          "Total Fat":" 67.5g",
          "Saturated Fat": "29.4g",
          "Cholesterol":"370mg",
          "Sodium" : "1514mg",
          "Total Carbohydrate":" 35g",
          "Dietary Fiber":"5.2g",
      },
      "calLevel": "Very High"
    },


    {
        "idMeal": "07",
        "mealName": "Cream Cheese Tart",
        "category": ["Starter", "Breakfast"],
        "area": "Russian",
        "instructions": "Crush the meat so that it is finite and we put it on a griddle to brown. Put the eggs, bacon and ham to fry.\r\nCut the bread in half, put the beef brisket, the fried eggs, the bacon, the ham, the mozzarella, the tomato and the lettuce. Cover with the other half of the bread and serve.",
      "mealThumb": "https://www.themealdb.com/images/media/meals/wurrux1468416624.jpg",
      "youtube":  "https://www.youtube.com/embed/UhQPwO4uymo",
      "ingredientsMeasuers": {
        "Flour":"250g",
        "Butter":"125g",
        "Egg":"1",
        "Salt":"Pinch",
        "Cheese":"300g",
        "Milk":"100ml milk",
        "Eggs":"3",
        "Parmesan Cheese":"100g",
        "Plum tomatoes":"350g",
        "White Vinegar":"3tbsp",
        "Honey":"1 tbsp",
        "Basil":"Topping",
      },
      "rating": 4,
      
      "nutritionFacts": {
          "Calories": 362,
          "Total Fat":"20g ",
          "Cholesterol":"43mg",
          "Sodium": "265mg",
          "Carbohydrate": "42g",
          "Protein": "4g"
      },
      "calLevel": "High"
    },



     {
        "idMeal": "08",
        "mealName": "Flamiche",
        "category": ["Starter", "Vegetarian"],
        "area": "French",
        "instructions": "For the pastry, sift the flour and salt into the bowl of a food processor, add the butter and lard, then whizz together briefly until the mixture looks like fine breadcrumbs. Tip the mixture into a bowl, then stir in the cheese and enough of the water for the mixture to come together. Tip out onto a lightly floured surface and knead briefly until smooth. Roll out thinly and line a 23cm x 4cm loose-?bottomed fluted flan tin. Prick the base with a fork. Chill for 20 minutes.\r\n02.Melt the 75g butter in a saucepan over a low heat, then add the leeks and the salt. Cover and cook for ?10 minutes until soft. Uncover the pan, increase the heat and cook ?for 2 minutes, stirring occasionally, until the liquid has evaporated. Spoon onto a plate and leave to cool.\r\n03.Preheat the oven to 200°C/fan180°C/gas 6. Line the pastry case with baking paper and baking beans or rice and blind bake for 15-20 minutes until the edges are biscuit-coloured. Remove the paper and beans/rice and return the case to the oven for 7-10 minutes until the base is crisp and lightly golden. Remove and set aside. Reduce the oven temperature to 190°C/fan170°C/gas 5.\r\n04.Put the crème fraîche into a bowl with the whole egg, egg yolks and nutmeg. Lightly beat together, then season. Stir in the leeks. Spoon ?the mixture into the tart case and bake for 35-40 minutes until set ?and lightly golden. Remove from ?the oven and leave for 10 minutes. Take out of the tin and serve.",
      "mealThumb": "https://www.themealdb.com/images/media/meals/wssvvs1511785879.jpg",
      "youtube":  "https://www.youtube.com/embed/LxTPzwCyeNo",
      "ingredientsMeasuers": {
        "Butter":"75g",
        "Leek":"1kg",
        "Salt":"½ tsp",
        "Creme Fraiche":"300ml",
        "Egg":"1",
        "Egg Yolks":"3",
        "Nutmeg":"¼ teaspoon",
        "Plain Flour":"225g",
        "Salt":"½ tsp",
        "Butter":"60g",
        "Lard":"60g",
        "Cheddar Cheese":"50g",
        "Water":"2 tbs",
      },
      "rating": 2,

       "nutritionFacts": {
          "Calories": 637,
          "Total Fat":"37g",
          "Saturates":"20g",
          "Carbs":"52g",
          "Sodium": "265mg",
          "Sugars": "4g",
          "Fibre": "6g",
          "Protein":"22g",
          "Salt":"1.7g",
      },
      "calLevel": "Very High"
    },

    {
        "idMeal": "09",
        "mealName": "Egg Drop Soup",
        "category": ["Starter", "Vegetarian"],
        "area": "Chinese",
        "instructions": "In a wok add chicken broth and wait for it to boil.\r\nNext add salt, sugar, white pepper, sesame seed oil.\r\nWhen the chicken broth is boiling add the vegetables to the wok.\r\nTo thicken the sauce, whisk together 1 Tablespoon of cornstarch and 2 Tablespoon of water in a bowl and slowly add to your soup until it's the right thickness.\r\nNext add 1 egg slightly beaten with a knife or fork and add it to the soup slowly and stir for 8 seconds\r\nServe the soup in a bowl and add the green onions on top.",
        "mealThumb": "https://www.themealdb.com/images/media/meals/1529446137.jpg",
        "youtube":  "https://www.youtube.com/embed/9XpzHm9QpZg",
        "ingredientsMeasuers": {
        "Chicken Stock":"3 cups",
        "Salt":"1/4 tsp",
        "Sugar":"1/4 tsp",
        "Pepper":"pinch",
        "Sesame Seed Oil":"1 tsp",
        "Peas":"1/3 cup",
        "Mushrooms":"1/3 cup",
        "Cornstarch":"1 tbs",
        "Water":"2 tbs",
        "Spring Onions":"1/4 cup",
      },
      "rating": 2,

       "nutritionFacts": {
          "Calories": 98,
          "Total Fat":"4.7g",
          "Cholesterol": "157mg",
          "Sodium": "2056mg",
          "Total Carbohydrates": "9g",    
      },
      "calLevel": "Low"
    },


    {
        "idMeal": "10",
        "mealName": "Crispy Eggplant",
        "category": ["Starter", "Vegetarian"],
        "area": "Filipino",
        "instructions": "Slice eggplant into 1 cm (0.4-inch) slices. Place them in a bowl and sprinkle them with salt. allow them to sit for 30 minutes to render some of their liquid and bitterness.\r\n2. After 30 minutes wash eggplant slices from salt and pat dry with a kitchen towel.\r\n3. In a large bowl/plate place breadcrumbs and sesame seeds. In another bowl beat 2 eggs with pinch salt and pepper.\r\n4. Heal oil in a large skillet over high heat.\r\n5. Dip eggplant slices in egg, then in crumbs, and place in hot oil. Fry 2 to 3 minutes on each side, or until golden brown. Drain on a paper towel. \r\n",
      "mealThumb": "https://www.themealdb.com/images/media/meals/c7lzrl1683208757.jpg",
      "youtube":  "https://www.youtube.com/embed/4mINk5d2hto",
      "ingredientsMeasuers": {
        "Egg Plants":"1 large",
        "Breadcrumbs":"1 cup",
        "Sesame Seed":"50g",
        "Eggs":"2",
        "Salt":"To taste",
        "Pepper":"To taste",
        "Vegetable Oil":"For frying",  
      },
      "rating": 4,
       "nutritionFacts": {
          "Calories": 475,
          "Total Fat":"28g",
          "Protein":"8g",
          "Carbohydrate": "49g",
          "Sugar": "3.9g",
          "Dietary Fiber": "4.5g",    
      },
      "calLevel": "High"
    },
]

# ROUTES
@app.route('/')
def welcome():
   return render_template('main.html', meals=meals)  
 

@app.route('/view/<id>')
def recipe_page(id):
    selected_meal = next((meal for meal in meals if meal["idMeal"] == id), None)
    if selected_meal:
        # Pass the selected meal data to the template
        return render_template('popular.html', meal=selected_meal, meals=meals)
    else:
        # If no meal with the provided idMeal is found, return a 404 error page
        return render_template('error.html', meals=meals)


@app.route('/search_results/<input>')
def results_page(input):  
    input_lower = input.lower()

    # Perform filtering
    search_results = [
        meal for meal in meals if 
        input_lower in meal['mealName'].lower() or
        any(input_lower in field.lower() for field in [' '.join(meal['category']), meal['area'].lower()]) or
        input_lower in meal['calLevel'].lower()
    ]
    # Extract meal names from search_results
    meal_names = [meal['mealName'] for meal in search_results]

    # Return the results or render a template with the results
    return render_template('results.html', search_results=search_results, input=input, meals=meals, meal_names=meal_names)
    

@app.route('/add', methods=['GET','POST'])
def add_data():
    if request.method == 'GET':
        # Handle GET request (render the form)
        return render_template('addData.html', meals=meals)
    elif request.method == 'POST':
        # Handle POST request (process form submission)
        data = request.json
        
        if isinstance(data, dict):
            
            if 'rating' in data:
                data['rating'] = int(data['rating'])

            data['idMeal'] = str(len(meals) + 1)

            meals.append(data)

        return data 
    else:
        return "Invalid data format"
   

@app.route('/edit/<id>', methods=['GET','POST'])
def edit_data(id):
    if request.method == 'GET':
      id = str(id)
      
      # Find the meal with the matching id
      selected_meal = None
      for meal in meals:
          if meal["idMeal"] == id:
              selected_meal = meal
              break
      
      return render_template('editData.html', meal=selected_meal, meals=meals)
    
    elif request.method == 'POST':
        data = request.json
        idMeal = data.get('idMeal')

        for meal in meals:
          if meal['idMeal'] == idMeal:
              # Update the meal with the new data
              meal.update(data)
              break 
          
        return meal 
  

@app.route("/filter_by", methods=["POST"])
def filter_by():
      # Receive the data sent from the frontend
      checked_values = request.json
      filtered_meals = []
      for meal in meals:
          if (meal["calLevel"] in checked_values) or (meal["area"] in checked_values) or (any(category in checked_values for category in meal["category"])):
              filtered_meals.append(meal)
      
      response_data = {
        "checked_values": checked_values,
        "filtered_meals": filtered_meals
      }

      return jsonify(response_data)


@app.route("/display_filter_results", methods=["GET"])
def display_filter_results():
    
    meal_names=['']

    # Get the value of the 'idMeals' query parameter
    ids = request.args.get("ids")  
    checkedVals = request.args.get("checkedVals") 

    if ids:
      filtered_meals = [meal for meal in meals if meal['idMeal'] in ids]
     
      return render_template('results.html', search_results=filtered_meals, input=checkedVals, meals=meals, meal_names=meal_names)
    
    elif checkedVals:
      checked_values = checkedVals.split(",")

      filtered_meals = []

      for meal in meals:  
          if (meal["calLevel"] in checked_values) or (meal["area"] in checked_values):
              filtered_meals.append(meal)
          else:     
              for category in meal["category"]:
                  if category in checked_values:
                      filtered_meals.append(meal)
                      break  

      return render_template('results.html', search_results=filtered_meals, input=checkedVals, meals=meals, meal_names=meal_names)


if __name__ == '__main__':
   app.run(debug = True)




