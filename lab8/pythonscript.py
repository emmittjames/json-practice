import json, csv

with open('../data/schacon.repos.json', 'r') as jsonfile:
    with open('./chacon.csv', 'a') as csvfile:
        csv_writer = csv.writer(csvfile)
        data = json.load(jsonfile)
        for row in data[:5]:
            csv_entry = [row["name"], row["html_url"], row["updated_at"], row["visibility"]]
            csv_writer.writerow(csv_entry)
        
        