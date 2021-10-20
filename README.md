# challenge_API_deployment

- Repository: `challenge-api-deployment`
- Type of Challenge: `Learning`
- Duration: `5 days`
- Deadline: `30/07/2021 16:00` **(code)**
- Presentation: `02/08/2021 10:00`
- Team challenge : Solo

## Mission objectives

- Be able to deploy a machine learning model.
- Be able to create a Flask API that can handle a machine learning model.
- Deploy an API to Heroku with Docker.

----------------------------------------------------------------------------------------
Dependencies

- Scikit-learn
- Pandas
- Numpy
- json
- Flask

-------------------------------------------------------------------------------------------------
## Usage

This API has been deployed with heroku under the url: https://flaskapimo.herokuapp.com/
For the predictions, send a POST request to https://flaskapimo.herokuapp.com/predict with the following parameters:
``` data format for the POST request:
                {
                    "data": {"type": "APARTMENT" | "HOUSE" ,
                    "room_number": int,
                    "area": int,
                    "kitchen_equipped": bool 0 | 1,
                    "furnished": bool  0 | 1,
                    "fireplace": bool  0 | 1,
                    "terrace": bool  0 | 1,
                    "terrace_area": int,"garden": bool 0 | 1,
                    "garden_area": int,"land_surface": int,
                    "facade_count": int,
                    "swimming_pool": bool 0 | 1,
                    "building_condition": "TO_BE_DONE_UP" | "TO_RENOVATE" | "GOOD" | "JUST_RENOVATED" | "AS_NEW" | "TO_RESTORE",
                    "Province":"LUXEMBOURG" | "HAINAUT" | "FLANDRE-OCCIDENTALE" | "LIEGE" | "FLANDRE-ORIENTALE" | "BRUXELLES" |
                    "BRABANT FLAMAND" | "ANVERS" | "BRABANT WALLON" | "LIMBOURG" | "NAMUR"
                            
                    }
                }
                
```
