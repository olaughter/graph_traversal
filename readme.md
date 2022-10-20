# Graph Traversal

This repo is a response to a takehome interview assignment with the following brief (summarised):

Calculate the shortest route on a network of computers, implemented by a `route()` function. drawing on an sqlite database. The graph data is currently stored in an sql database, where there is a row for each connection, eg:

network_connectivity
| a   | b   |
| --- | --- |
| 1   | 2   |
| 1   | 6   |
| 2   | 3   |
| ... | ... |

# How to run

1. install poetry for dependency management
2. install dependencies: `poetry install`
3. Setup .env file by copying the sample and filling in relevant values (i.e. for a production version of the database)
4. Run `main.py` passing in desired values, eg: `poetry run python main.py 1 3`

Alternatively, do steps 2 and 3 then run the test cases defined in `test_main.py` via: `poetry run pytest`


# Assumptions

1. There is a tradeoff between wether to load all data in from the database and restructure it as a python data type, or wether to query the database for this each time it is needed instead. I have assumed that the table could be too large to load into memory, and also that user inputs in this instace have been sanitised. So the best option therefore is to query the database directly as needed.

2. Although it wasnt stated, the nature of the tasks suggests that the traversal should be bidirectional