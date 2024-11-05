#!/usr/bin/python3
"""
Create a Python function that generates personalized invitation files from
a template with placeholders and a list of objects.
"""


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template with placeholders
    and a list of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list of dict): A list of dictionaries where each
        dictionary represents an attendee
            with keys as placeholders and values as the corresponding data.
    """

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation_text = template
        for key, value in attendee.items():
            placeholder = "{" + key + "}"
            if value is None:
                value = "N/A"
            invitation_text = invitation_text.replace(placeholder, value)

        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(invitation_text)
