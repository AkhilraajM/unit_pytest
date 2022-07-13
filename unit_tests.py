import pytest
import requests
import json


# Give your URL
URL = "https://reqres.in/"

# change the meaningful name for the test case
def test_case1():
    # change the subdirectory as per the URL
    subdirectory= "api/users/2"

    # change the .get .put .post according to the request 
    response = requests.get(URL+subdirectory)
    
    # asserting status code
    # replace 200 400 500 or any accordingly
    assert response.status_code == 200

    # JSON response you are expecting
    test_data_json = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
    }

    # To verify all the data together
    assert json.loads(response.text) == test_data_json

    # To verify particular item in the response body/request

    data_from_api = json.loads(response.text)
    
    # For example we will assert id 

    assert data_from_api["data"]["id"] == 2

