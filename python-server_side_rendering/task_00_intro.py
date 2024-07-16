#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date if event_date else "N/A",
            event_location=event_location
        )

        output_filename = f"output_{index + 1}.txt"

        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)

        print(f"Generated {output_filename}")
