#Getting User for Weather Input
current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Initializing clothing recommandation variable
clothing_recommandation = ""

#Checking weather and recommending clothing
if current_weather == "sunny":
	clothing_recommandation = "Wear a t-shirt and sunglasses."
elif current_weather == "rainy":
	clothing_recommandation = "Don't forget your umbrella and a raincoat."
elif current_weather == "cold":
          clothing_recommandation = "Make sure to wear a warm coat and a scarf."
else:
	clothing_recommandation = "Sorry, I don't have recommendations for this weather."

#Printing the weather recommandation
print(clothing_recommandation)