import json 

# test main if status code 200
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

json_file={
    "no2":36.255351616,
    "pm2.5":78.0,
    "o3":44.0,
    "leto_od":2023.0,
    "mesec_od":2.0,
    "dan_od":15.0,
    "ura_od":19.0,
    "min_od":0.0,
    "leto_do":2023.0,
    "mesec_do":2.0,
    "dan_do":15.0,
    "ura_do":20.0,
    "min_do":0.0
}

# send json data and check if status code 200
def test_json_data(client):
    response = response = client.post("/air/predict/", data=json.dumps(json_file), headers={"Content-Type": "application/json"})
    assert response.status_code == 200