# 4-4-5_calendar

With a 4-4-5 calendar, the standard 52-week year divides into four 13-week quarters, which comprise three periods split into a four-week, four-week, five-week format. A twist to this uniform structure occurs every five or six years when a fifty-third week is necessary to catch up for leap years and the fact that the standard 52-week year accounts for only 364 days.

Retailers are the most common users of the 4-4-5 calendar. Companies who use the weeks-based calendar often do so when there is a natural alignment with core business flows. These flows include customer traffic, shipping, payroll processing, and procurement. These firms often find that period-end cutoff is less complex for those costs, and there is better matching of costs and revenues.


# FiscalYear 4-4-5_calendar Back-end

This is an api for the  FiscalYear 4-4-5_calendar system built with the Django REST Framework.

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

**/<year>**

* GET
**url/2021**

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
 

 ## Deploment process

 # Documentation


 # Notes: https://cloudacademy.com/blog/zappa-or-how-to-go-serverless-with-django/

 ## def get(self, request,year):
    - calculate the date of the first monday of the year
    - loop for the 4th quarters
    - On the quarter there is a 2 months with 4 weeks and one with 5 weeks
    - It specify the fiscal month name
    - It specify the number of weeks for the month
    - loops to create the weeks data og the month
    - specify the week number
    - specify the days dates for the week
    - add the week data to the week number
    - specify the next week number
    - specify the month week data
    - add the current month to the months
    - add one to the month number to prepare to the next month name
