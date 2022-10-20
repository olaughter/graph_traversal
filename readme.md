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

Alternatively, do steps 2 and 3 then run test cases via: `poetry run pytest`