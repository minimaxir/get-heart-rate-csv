import re
import csv

file_name = 'export.xml'
pattern = '^.*IdentifierHeartRate".*startDate="(.{19}).*value="([0-9]*).*$'

with open('hr_export.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['dt', 'bpm'])

    with open(file_name, 'r') as f2:
        for line in f2:
            search = re.search(pattern, line)
            if search is not None:
                writer.writerow([search.group(1), search.group(2)])
