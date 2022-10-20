import argparse
import os
import sqlite3

from dotenv import load_dotenv

class Database:
    def __init__(self) -> None:
        database = os.environ["NETWORK_DATABASE"]
        self.conn = sqlite3.connect(database)


    def get_children(self, parent, already_reviewed):
        """Retrieve all children of a given node from the database

        To support bidirectional travelling we check both columns

        Note, this could have also been implemented via a python lookup table if memory constraints where not a factor.

        Args:
            parent (int): node to find children for
            already_reviewed (list): nodes that have already been travelled down and should not be considered for a route
        Returns:
            list: child nodes
        """
        cursor = self.conn.execute(f"select * from network_connectivity where a={parent} or b={parent}")
        
        children = []
        for row in cursor:
            for value in row:
                if value != parent and value not in already_reviewed:
                    children.append(value)

        return list(set(children))


def valid_paths_remain(current_layer, already_reviewed):

    fresh_routes = []

    for route in current_layer:
        if route[-1] not in already_reviewed:
            fresh_routes.append(True)
    return any(fresh_routes)


def route(start, target):
    db = Database()
    already_reviewed = []
    next_layer = [[start]]

    while True:
        current_layer = next_layer
        next_layer = []

        if not valid_paths_remain(current_layer, already_reviewed):
            raise Exception("Potential paths exhausted, no solution possible")

        for route in current_layer:
            node = route[-1]
            already_reviewed.append(node)
            children = db.get_children(node, already_reviewed)

            if target in children:
                route.append(target)
                return route
            else:
                for child in children:
                    new_route = route.copy()
                    new_route.append(child)
                    next_layer.append(new_route)


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Finds the shortest communication path between two nodes in the network."
        )

    parser.add_argument("start", type=int)
    parser.add_argument("target", type=int)

    args = parser.parse_args()

    route(args.start, args.target)