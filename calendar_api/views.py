

from .serializers import calendarSerializer
import datetime



from rest_framework.views import APIView
from rest_framework.response import Response

class calendarView(APIView):

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