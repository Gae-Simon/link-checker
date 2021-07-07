from datetime import datetime, time, date

# Webbrowser
import webbrowser
import requests

print("Inserting Sources....")

# Data
with open("sources.txt", "r") as data, open("final_sources.txt", "w") as final_data:
  # Create Lists
  sources = [x.strip() for x in data.readlines()]
  available_sources = []
  unavailable_sources = []

  # Output List
  print(sources)
  print("Sources successfully inserted!")

  # check if the sources are available
  print("Check if Website is available...")
  for src in sources:
      try:
          res = requests.get(src)
          if res.status_code == 200:
              print("Website exists:", src)
              available_sources.append(src)
          else:
              print("ERROR")
      except Exception:
          print("Website does not exist:", src)
          unavailable_sources.append(src)

  print("Check completed!")

  # Writing Sourcefile
  print("Writing final source data...")
  final_data.write("Sources are checked and available:\n")
  for available in available_sources:
      dt = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      final_data.write(f"{available}; [{dt} Uhr]\n")

  final_data.write("\n")

  for unavailable in unavailable_sources:
      final_data.write("Sources are unavailable:\n")
      final_data.write(f"{unavailable}\n")

print("Writing completed!")