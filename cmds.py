from businesses import Businesses
from reviews import Reviews



def letsBegin(db):
    
    businesses = Businesses(db)
    reviews = Reviews(db)

    running = True

    while True:
        printAllOptions()
        userInput = input("\nWhat would you like to do? ")
        match userInput:
            case "1":
                data = businesses.floridaPizzaQuery()
                data = round(data, 2)
                print("Floridians average pizza rating is : " + str(data) + " out of 5")

            case "2":
                data = businesses.californiaMexicanQuery()
                data = round(data, 2)
                print("Californians average mexican rating is : " + str(data) + " out of 5")

            case "3":
                data = businesses.PhiladelphiaBarQuery()
                data = round(data, 2)
                print("Philadelphia average bar rating is : " + str(data) + " out of 5")

            case "4":
                data = reviews.mostReviewsQuery()
                print("State with most reviews: ")
                print(data[0] + " with " + str(data[1]) + " reviews")

            case "5":
                data = reviews.listTop10statesReviewed()
                print("Top 10 states with most reviews: ")
                for row in data:
                    print(row[0] + " with " + str(row[1]) + " reviews")

            case "6":
                state = input("Enter a state: ")
                t = input("Enter a type of restaurant: ")
                data = businesses.getCountOfTypeOfRestaurantsByState(t, state)
                print("There are " + str(data) + " " + t + " restaurants in " + state)

            case "7":
                state = input("Enter a state: ")
                t = input("Enter a type of restaurant: ")
                data = businesses.getTopRatedRestaurantByType(t, state)
                if data is None:
                    print("No data found")
                    continue
                businesses.printBusinessInfo(data)

            case "8":
                state = input("Enter a state: ")
                city = input("Enter a city: ")
                t = input("Enter a type of restaurant: ")
                data = businesses.getTopRatedRestaurantByTypeCityState(t, state, city)
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

            case "10":
                state = input("Enter a state: ")
                t = input("Enter a type of restaurant: ")
                data = reviews.getReviewsForTopRatedRestaurantByType(t, state)
                for row in data:
                    reviews.printReviewData(row)

            case "11":
                # TODO
                pass


            case "12":
                name = input("Enter a business name: ")
                data = reviews.get5RandomReviewsForRestaurantByName(name)
                for row in data:
                    reviews.printReviewData(row)

            case "13":
                businesses.printBusinessInfo(businesses.getMostReviewedRestaurants())

            case "14":
                businesses.printBusinessInfo(businesses.getHighestRatedRestaurants())


            case "exit":
                print("Goodbye!")
                return

            case _:
                print("Invalid input. Please try again. " + userInput)


def printAllOptions():
    print("\nOptions:")
    print("1. Get average pizza rating for Florida")
    print("2. Get average mexican rating for California")
    print("3. Get average bar rating for Philadelphia")
    print("4. Get state with most reviews")
    print("5. Get top 10 states with most reviews")
    print("6. Get count of type of restaurants by state")
    print("7. Get top rated restaurant by type")
    print("8. Get top rated restaurant by type, city, and state")
    print("9. Get businesses by state and name")
    print("10. Get reviews for top rated restaurant by type")
    # print("11. Get reviews for top rated restaurant by type (lowest)")
    print("12. Get 5 random reviews for restaurant by name")
    print("13. Get most reviewed restaurants")
    print("14. Get highest rated restaurants")
    print("exit. Exit program\n")
