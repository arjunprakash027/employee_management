## Useage

A system to be able to manage data for employees. Requests will be accepted over HTTP ([API contract](#api-contract)). No databases/libraries is used to store/maintain data.


### Setup guide
Install docker and build and run the dockerfile


### Technical details
1. repository has a `Dockerfile` that starts your HTTP web app
2. HTTP app exposes APIs ([API contract](#api-contract)) on port 8080
3. No existing databases, libraries and services is used to store data
4. Application persists data across restarts
5. Data persisted in `/home/data`


#### Data to be stored

{
    employeeId: string,
    name: string,
    city: string
}


#### API contract
##### GET /greeting
  Checks whether the service is available.

###### Response
* Code: 200  
* Content: `Hello world!` 


##### POST /employee
Creates a new Employee and returns the employeeId

###### Request & Response headers
Content-Type: application/json

###### Body

{
    name: string,
    city: string
}


###### Success Response
* Status code: 201
* Content: `{ "employeeId": "<employee_id>" }` (Note: Employee ID is a `string`)


##### GET /employee/:id
Returns the specified employee.

###### URL Params
`id=[string]` Required

###### Success Response
* Status code: 200
* Content: `{ <employee_object> }`

###### Error Response
* Status code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`


##### GET /employees/all
Returns list of all employees.

###### Success Response
* Status code: 200
* Content: `[{ <employee_object> }]`


##### PUT /employee/:id
Updates fields of the existing employee and returns the new object.

###### URL Params
`id=[string]` Required

###### Headers
Content-Type: application/json

###### Body

{
    name: string,
    city: string
}


###### Success Response
* Code: 201
* Content: `{ <employee_object> }`

###### Error Response
* Code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`


##### DELETE /employee/:id
  Deletes existing employee record.

###### URL Params
`id=[string]` Required

###### Success Response
* Status code: 200
* Content:  `{ <employee_object> }`

###### Error Response
* Status code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`
