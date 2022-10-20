import argparse
import os
import sqlite3

from dotenv import load_dotenv


def route(start, target):
    return []


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Finds the shortest communication path between two nodes in the network."
        )

    parser.add_argument("start", type=int)
    parser.add_argument("target", type=int)

    args = parser.parse_args()

    route(args.start, args.target)