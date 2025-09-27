import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output_text = template.replace("{name}", attendee.get("name", "N/A"))
        output_text = output_text.replace("{event_title}", attendee.get("event_title", "N/A"))
        output_text = output_text.replace("{event_date}", attendee.get("event_date", "N/A"))
        output_text = output_text.replace("{event_location}", attendee.get("event_location", "N/A"))

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(output_text)

        print(f"Created {filename}")
