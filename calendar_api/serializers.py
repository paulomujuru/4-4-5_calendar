from rest_framework import serializers


class weeksSerializer(serializers.Serializer):
    weekNumber = serializers.IntegerField()
    days = serializers.ListField(child=serializers.DateTimeField(format="%Y-%m-%d"))

class monthsSerializer(serializers.Serializer):
    fiscalMonth = serializers.CharField()
    NumberOfWeeks = serializers.IntegerField()
    weeks = serializers.ListField(child=weeksSerializer())

class calendarSerializer(serializers.Serializer):

   FiscalYear = serializers.IntegerField()
   months = serializers.ListField(child=monthsSerializer())