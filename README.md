# 4-4-5_calendar

With a 4-4-5 calendar, the standard 52-week year divides into four 13-week quarters, which comprise three periods split into a four-week, four-week, five-week format. A twist to this uniform structure occurs every five or six years when a fifty-third week is necessary to catch up for leap years and the fact that the standard 52-week year accounts for only 364 days.

Retailers are the most common users of the 4-4-5 calendar. Companies who use the weeks-based calendar often do so when there is a natural alignment with core business flows. These flows include customer traffic, shipping, payroll processing, and procurement. These firms often find that period-end cutoff is less complex for those costs, and there is better matching of costs and revenues.


# FiscalYear 4-4-5_calendar Back-end

This is an api for the  FiscalYear 4-4-5_calendar system built with the Django REST Framework.

## LINK:

https://paulojunior.pythonanywhere.com/2021?format=json

## Running Locally

1. Clone this repo
1. cd into this repo
1. Create a python virtual environment: `pipenv install`
1. Activate virutal environment: `pipenv shell`
1. Install packages in the Pipfile: `pipenv install`
1. `pip install -r requirements.txt`
1. Run the project: `python manage.py runserver`

## Schema

* No usage of a database because there is no need to store the calendar in a database.

## API USAGE

https://paulojunior.pythonanywhere.com/[year]?format=json

* GET
/[year]

## Calendar View

{
"FiscalYear": 2021,
"months": [
{
"fiscalMonth": "January",
"NumberOfWeeks": 4,
"weeks": [
{
"weekNumber": 1,
"days": [
"2021-01-04",
"2021-01-05",
"2021-01-06",
"2021-01-07",
"2021-01-08",
"2021-01-09",
"2021-01-10"
]
},
{
"weekNumber": 2,
"days": [
"2021-01-11",
"2021-01-12",
"2021-01-13",
"2021-01-14",
"2021-01-15",
"2021-01-16",
"2021-01-17"
]
},
{
"weekNumber": 3,
"days": [
"2021-01-18",
"2021-01-19",
"2021-01-20",
"2021-01-21",
"2021-01-22",
"2021-01-23",
"2021-01-24"
]
......
}
]
}
]
}
 
 
 ##  AWS Deploment process
# Zappa
1. Request comes into API Gateway
2. Gateway fires up the server inside a lambda function
3. The server is then feed to the request
4. Handled the Django app through the WSGI layer

 # Documentation


 # Notes: https://cloudacademy.com/blog/zappa-or-how-to-go-serverless-with-django/

