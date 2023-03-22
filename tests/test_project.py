import json 

# test main if status code 200
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

json_file={
    "pm2.5": 8.0,
    "o3": 57.0,
    "no2": 25.0,
    "temps": 11.3
}

# send json data and check if status code 200
# def test_json_data(client):
#     response = response = client.post("/air/predict/", data=json.dumps(json_file), headers={"Content-Type": "application/json"})
#     assert response.status_code == 200


