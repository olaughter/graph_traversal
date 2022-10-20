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

