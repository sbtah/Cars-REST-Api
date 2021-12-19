# This is a simple RESTApi that I have build as a part of a recruitment test.
# ENDPOINTS:

POST /cars

Request body should contain car make and model name
Based on this data, its existence should be checked here https://vpic.nhtsa.dot.gov/api/
If the car doesn't exist - return an error
If the car exists - it should be saved in the database
POST /cars/

Content-Type: application/json;charset=UTF-8

{

"make" : "Volkswagen",

"model" : "Golf",

}

DELETE /cars/{ id }

Should delete the car with the given id from database
If the car doesn't exist in database - return an error
DELETE /cars/{ id }/

POST /rate

* Add a rate for a car from 1 to 5

POST /rate/

Content-Type: application/json;charset=UTF-8

{

"car_id" : 1,

"rating" : 5,

}

GET /cars

Should fetch a list of all cars already present in application database with their current average rate
GET /cars/

Content-Type: application/json;charset=UTF-8

Response:

[

{

"id" : 1,

"make" : "Volkswagen",

"model" : "Golf",

"avg_rating" : 5.0,

},

{

"id" : 2,

"make" : "Volkswagen",

"model" : "Passat",

"avg_rating" : 4.7,

}

]

GET /popular

Should return top cars already present in the database ranking based on a number of rates (not average rate values, it's important!)
GET /popular/

Content-Type: application/json;charset=UTF-8

Response:

[

{

"id" : 1,

"make" : "Volkswagen",

"model" : "Golf",

"rates_number" : 100,

},

{

"id" : 2,

"make" : "Volkswagen",

"model" : "Passat",

"rates_number" : 31,

}

]