from datetime import datetime, time, date

print("Inserting Sources....")

# Data
data = open("sources.txt", "r")
final_data = open("final_sources.txt", "w")

# Webbrowser
import webbrowser
import requests

# Create Lists
sources = []
available_sources = []
unavailable_sources = []


# Read Lines and save them in a List
for line in data:
    sources.append(line)

# Output List
print(sources)
print("Sources successfully inserted!")

# check if the sources are available
print("Check if Website is available...")
for x in range(len(sources)):
    request = requests.get(sources[x-1])
    if request.status_code == 200:
        print("Website exists: " + sources[x-1].replace("\n", ""))
        available_sources.append(sources[x-1])
    else:
        print("Website does not exist: " + sources[x-1].replace("\n", ""))
        unavailable_sources.append(sources[x-1])

print("Check completed!")

# Writing Sourcefile
final_data.write("Sources are checked and available: " + "\n")
for x in range(len(available_sources)):
    now = datetime.now()
    current_datetime = now.strftime("%m/%d/%Y, %H:%M:%S")
    final_data.write(available_sources[x-1].replace("\n", "") + "; [" + current_datetime + " Uhr]" + "\n")
