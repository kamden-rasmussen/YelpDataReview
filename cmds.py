from businesses import Businesses
from reviews import Reviews



def letsBegin(db):
    
    businesses = Businesses(db)
    reviews = Reviews(db)

    running = True

    while True:
        userInput = input("\nWhat would you like to do? ")
        match userInput:
            case "1":
                print("You entered 1")
                data = businesses.floridaPizzaQuery()
                data = round(data, 2)
                print("Floridians average pizza rating is : " + str(data) + " out of 5")

            case "2":
                print("You entered 2")
                data = businesses.californiaMexicanQuery()
                data = round(data, 2)
                print("Californians average mexican rating is : " + str(data) + " out of 5")

            case "3":
                print("You entered 3")
                data = businesses.PhiladelphiaBarQuery()
                data = round(data, 2)
                print("Philadelphia average bar rating is : " + str(data) + " out of 5")

            case "4":
                print("You entered 4")
                data = reviews.mostReviewsQuery()
                print("State with most reviews: ")
                print(data[0] + " with " + str(data[1]) + " reviews")

            case "5":
                print("You entered 5")
                data = reviews.listTop10statesReviewed()
                print("Top 10 states with most reviews: ")
                for row in data:
                    print(row[0] + " with " + str(row[1]) + " reviews")

            case "6":
                print("You entered 6")
                state = input("Enter a state: ")
                t = input("Enter a type of restaurant: ")
                data = businesses.getCountOfTypeOfRestaurantsByState(t, state)
                print("There are " + str(data) + " " + t + " restaurants in " + state)

            case "7":
                print("You entered 7")
                state = input("Enter a state: ")
                t = input("Enter a type of restaurant: ")
                data = businesses.getTopRatedRestaurantByType(t, state)
                if data is None:
                    print("No data found")
                    continue
                businesses.printBusinessInfo(data)


            case "9":
                state = input("Enter a state: ")
                business = input("Enter a business: ")
                data = businesses.getBusinessesByStateAndName(state, business)
                for row in data:
                    businesses.printBusinessInfo(row)

            case "exit":
                print("Goodbye!")
                return

            case _:
                print("Invalid input. Please try again. " + userInput)
