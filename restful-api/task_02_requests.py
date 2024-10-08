#!/usr/bin/python3
"""
This script fetches data from an API and provides utility functions for
printing and saving posts from a JSON response to a CSV file.
"""

import requests
import csv

r = requests.get('https://jsonplaceholder.typicode.com/posts')

filename = "posts.csv"


def fetch_and_print_posts():
    """
    Fetches posts from an API and prints the title of each post.

    Prints the status code of the HTTP request, and if the request
    is successful
    (status code 200), it prints the title of each post retrieved
    from the JSON response.

    Returns:
        None
    """
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()

    for post in posts:
        print(f"{post['title']}")


def fetch_and_save_posts():
    """
    Fetches posts from an API and saves them to a CSV file.

    If the request is successful (status code 200), it writes the
    posts to a CSV file
    with columns for 'id', 'title', and 'body'. The CSV file is
    saved as 'posts.csv'.

    Returns:
        None
    """
    if r.status_code == 200:
        posts = r.json()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()

        for post in posts:
            writer.writerow(
                {"id": post["id"],
                 "title": post["title"],
                 "body": post["body"]})
