import requests
import csv
import sys

def consume_api(city):
    response = requests.get('http://api.goeuro.com/api/v2/position/suggest/en/{0}' .format(city))
    relevant_data = [[i["_id"],i["type"], i["name"], i["geo_position"]["latitude"], i["geo_position"]["longitude"]]
                for i in response.json() ]
    return relevant_data

def to_csv(json_obj, _file="go_euro_output.csv"):
    with open(_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for result in json_obj:
            writer.writerow(result)

if __name__ == "__main__":
    city = sys.argv[1]
    output_file = "output_for_%s.csv" % city
    response = consume_api(city)
    to_csv(response, output_file)
