#!/usr/bin/python3

def generate_invitations(template, attendees):
    # Type check
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    for person in attendees:
        if not isinstance(person, dict):
            print("Error: attendees must be a list of dictionaries.")
            return

    # Empty checks
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    # Process attendees
    for i, person in enumerate(attendees, start=1):
        content = template

        name = person.get("name", "N/A")
        title = person.get("event_title", "N/A")
        date = person.get("event_date", "N/A")
        location = person.get("event_location", "N/A")

        if name is None:
            name = "N/A"
        if title is None:
            title = "N/A"
        if date is None:
            date = "N/A"
        if location is None:
            location = "N/A"

        content = content.replace("{name}", str(name))
        content = content.replace("{event_title}", str(title))
        content = content.replace("{event_date}", str(date))
        content = content.replace("{event_location}", str(location))

        filename = "output_{}.txt".format(i)

        with open(filename, "w") as file:
            file.write(content)
