from .serializers import calendarSerializer
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

class calendarView(APIView):
    
    '''
    The class:
    calculate the date of the first monday of the year
    loop for the 4th quarters
    On the quarter there is a 2 months with 4 weeks and one with 5 weeks
    It specify the fiscal month name
    It specify the number of weeks for the month
    loops to create the weeks data og the month
    specify the week number
    specify the days dates for the week
    add the week data to the week number
    specify the next week number
    specify the month week data
    add the current month to the months
    add one to the month number to prepare to the next month name
    
    '''

    def get(self, request,year):
        first_monday = datetime.datetime(int(year),1,7) + datetime.timedelta(days=-datetime.datetime(int(year),1,7).weekday())
        month_list=['January','February','March','April','May','June','July','August','September','October','November','December']
        weekNumber=1
        monthNumber=0
        months=list()
        for p in range(4):
            for j in [4,4,5]:
                month=dict()
                month["fiscalMonth"]=month_list[monthNumber]
                month['NumberOfWeeks']=j
                weeks = list()
                for k in range(0,j):
                    
                    week = dict()
                    week["weekNumber"]=weekNumber
                    days = list()
                    for i in range(0,7):
                        days.append((first_monday+datetime.timedelta(days=i+(weekNumber-1)*7)))
                    week["days"]=days
                    weeks.append(week)
                    weekNumber = weekNumber + 1
                month["weeks"]=weeks
                months.append(month)
                monthNumber+=1

        data = {"FiscalYear":int(year),"months":months}

        results = calendarSerializer(data).data
        return Response(results)