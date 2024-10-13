from bs4 import BeautifulSoup
import requests
import re

def event_grabber():
    response = requests.get("https://mason360.gmu.edu/mobile_ws/v17/mobile_events_list?range=0&limit=50&filter4_contains=OR&filter4_notcontains=OR&order=undefined&search_word=&&1728715900675")
    soup = BeautifulSoup(response.text, "html.parser")

    events = []

    if response.status_code == 200:
        data = response.json()
        for event in data:
            event_name = event.get("p3")  # eventName
            event_dates = event.get("p4")  # eventDates
            event_place = event.get("p6")
            event_url = event.get("p18")  # eventUrl
            event_tags = event.get("p22")  # tags the <p> with aria-labels)

            # Check if the event name is not "False"
            if event_name != "False":
                full_url = f"https://mason360.gmu.edu{event_url}"
                event_dates = re.sub("<p style='margin:0;'>", "", event_dates).replace("</p>", "").strip()
                event_dates = event_dates.replace(" &ndash; ", " - ").replace("20249", "2024")

                # Extract aria-labels from the tags
                tags = []
                if event_tags:
                    tag_soup = BeautifulSoup(event_tags, "html.parser")
                    aria_labels = tag_soup.find_all("a", attrs={"aria-label": True})
                    for tag in aria_labels:
                        aria_label = tag["aria-label"]
                        aria_label = aria_label.replace("List all events filtered by ", "")
                        aria_label = aria_label.replace(" slash ", "/")
                        tags.append(aria_label)

                # Format the event details
                formatted_event = f"""
                Event: {event_name}
                Date: {event_dates}
                Location: {event_place}
                More Info: {full_url}
                Tags: {', '.join(tags) if tags else 'No tags available'}
                """
                events.append(formatted_event)  # Append the formatted event to the list
        all_events = ""
        # Print all formatted events
        for event in events:
            all_events += event
        return all_events
    else:
        print("Failed to connect")