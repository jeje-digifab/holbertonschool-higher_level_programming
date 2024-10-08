#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

import requests
import csv
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts')
# r.headers['content-type']

filename = "posts.csv"

def fetch_and_print_posts():
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()

    for post in posts:
        print(f"{post['title']}")


def fetch_and_save_posts():
    if r.status_code == 200:
        posts = r.json()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()

        for post in posts:
            writer.writerow({"id": post["id"], "title": post["title"], "body": post["body"]})








