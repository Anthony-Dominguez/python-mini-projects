import json


data = 'covert_json_cvs/input.json'


with open(data, 'r') as file:
    json_data = json.load(file)
    
headers = json_data[0].keys()

with open('covert_json_cvs/output.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for entry in json_data:
        row = [str(entry[header]) for header in headers]
        file.write(','.join(row) + '\n')

print("Conversion completed. Check output.csv file.")