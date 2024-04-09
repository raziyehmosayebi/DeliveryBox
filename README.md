# DeliveryBox
The first part of this repository provides three different model for a binary classifier to identify if a delivery request takes too much to be aknowledged or accepted by a biker or not. the EDA and model training is provided in jupyter notebook and the best model is used in a restapi. The Dockerfile and REST API are located in the "app" directory. 

the second part provides some analysis and investigations of fraud actions in delivery system.
## Docker Image
In order to build the docker image run the following command
```
docker build -t myapp .
```
## Curl Request
Use the following curl command to get the response:
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "deliverey_category_id": 0.0,
    "weekday": 7.0,
    "time_bucket": 76.0,
    "total_distance": 0.6333,
    "sum_product": 2.0,
    "final_customer_fare": 480000,
    "destination_hexagonID": 11569,
    "source_hexagonID": 13593
  }' \
  http://localhost:5000/predict
```
