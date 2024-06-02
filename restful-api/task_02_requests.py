#!/usr/bin/python3
"""Module compiled with python3"""

import requests
import csv


def fetch_and_print_posts():
    """
    Function to fetch and print posts from the JSONPlaceholder API.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = r.status_code
    data = r.json()

    print("Status Code: {}".format(status_code))
    """
    Print the HTTP status code
    """

    for post in data:
        """
        Loop through the posts and print the content
        """
        print("{}".format(post["title"]))


def fetch_and_save_posts():
    """
    Fetches posts from an API and saves them to a CSV file
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = r.json()

    with open('posts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for post in data:
            writer.writerow(
                {'id': post['id'], 'title': post['title'],
                 'body': post['body']})
