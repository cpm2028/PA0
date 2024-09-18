# the goal I have to solve is, with $10,000, can my friend Bella afford to go to Italy.
#Used the calculator app to solve the problem
#I'm going on a trip to Italy in April. I have 10,000 saved in my bank account. My flight is round trip and costs 1,785. Food will cost 100 a day. I am going for 7 days. My hotel will cost 145 per day. Additionally I have a budget of 500 to spend on additional things. How much money will it cost in order to go on my trip?
bank=(int)(input("How much do you have to spend on the trip? "))
flight=(int)(input("How much will your flight cost both ways? "))
food= (int)(input("How much will your food cost for the week? "))
days=(int)(input("How many days are you traveling for? "))
hotel=(int)(input("How much will your hotel cost each day? "))
ExtraMoney= (int)(input("How much money are you keeping on the side for the trip? "))
FoodWeek= food*days
HotelWeek=hotel*days
DayAmount=days
print("")
FoodWeek= food*DayAmount
print("")
HotelWeek=hotel*DayAmount
print("")
TotalCost= flight+FoodWeek+HotelWeek+ExtraMoney
print("")
if bank >= TotalCost:
    print("Your total cost for the week will be: $", TotalCost)
    print(print("You can afford to go to Italy for the week, you will have a leftover of: $", bank-TotalCost))
else:
    print("You cannot afford to go on your trip, your budget goes over by: $", bank-TotalCost)



