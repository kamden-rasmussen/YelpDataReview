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
                data = businesses.newYorkPizzaQuery()
                print("New Yorkers like pizza this much: " + str(data))

            case "2":
                print("You entered 2")
                data = businesses.californiaMexicanQuery()
                print("Californians like Mexican this much: " + str(data))

            case "3":
                print("You entered 3")
                data = businesses.utahSodaQuery()
                print("Utahns like soda this much: " + str(data))

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
