# YelpDataReview

> Due to the size of the dataset, all of the work was done via pair-programming on a single computer. The code was written in Python 3.10

# To set up this project and try it out on your own:
## Download the dataset:
visit https://www.yelp.com/dataset/download to download the data. Once data is downloaded, extract the files and create a new folder called *yelp_dataset* inside of this project and place the both ***yelp_academic_dataset_review.json*** and ***yelp_academic_dataset_business.json*** in the newly created folder. Feel free to delete the other extracted files as they were not used.

## DB setup:
> Using an M1 Chip, the initialization of the DB for reviews took over 80 minutes. It is recommended to use a newer computer, or stop the process after so long.

Run `setup.py` to properly populate your local db instance.

## Run the program:
The easiest way to run the program is by using `make run` in the terminal. The program will output a list of available commands for the user to run.

| Command | Description |
| --- | --- |
| 1. | Get average pizza rating for Florida |
| 2. | Get average mexican rating for California |
| 3. | Get average bar rating for Philadelphia |
| 4. | Get state with most reviews |
| 5. | Get top 10 states with most reviews |
| 6. | Get count of type of restaurants by state |
| 7. | Get top rated restaurant by type |
| 8. | Get top rated restaurant by type, city, and state |
| 9. | Get businesses by state and name |
| 10. | Get reviews for top rated restaurant by type |
| 12. | Get 5 random reviews for restaurant by name |
| 13. | Get most reviewed restaurants |
| 14. | Get highest rated restaurants |
| exit | Exit program |

# Business Table
| Column Name | Type |
| --- | --- |
| business_id | 
| name | VARCHAR |
| city | VARCHAR |
| state | VARCHAR |
| stars | INT |
| review_count | INT |
| categories | VARCHAR |

# Review Table
| Column Name | Type |
| --- | --- |
| review_id | VARCHAR | 
| business_id | VARCHAR |
| stars | FLOAT | 
| text | VARCHAR |
