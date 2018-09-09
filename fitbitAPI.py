#Utilizes the fitbit API to grab data to create reports 

import fitbit
import datetime

authd_client = fitbit.Fitbit('client id here', 'client secret here'
    ,access_token='access token here'
    , refresh_token='refresh token here')

outfile = open("output.txt", "a")
outfile.write("Period, Date, Sleep Start, Sleep End, Mins Asleep, Mins Awake, Times Awake, Mins Restless, Times Restless, Minutes Until Sleep, Minutes After Aleep, Mins in Bed\n")

def writeData(sDate, eDate, period):

    startDate = datetime.datetime.strptime(sDate, "%Y-%m-%d")
    reportingDate = startDate
    endDate = datetime.datetime.strptime(eDate, "%Y-%m-%d")

    while reportingDate <= endDate:
        response = authd_client.sleep(date=reportingDate, user_id=None)
        for thing in response["sleep"]:
            if thing["isMainSleep"] == True:
                start = thing["startTime"]
                end = thing["endTime"]
                asleepTime = thing["minutesAsleep"]

                awakeTime = thing["minutesAwake"]
                awakeNumber = thing["awakeningsCount"]

                restlessTime = thing["restlessDuration"]
                restlessNumber = thing["restlessCount"]

                fallAsleep = thing["minutesToFallAsleep"]
                lieIn = thing["minutesAfterWakeup"]

                inBedTime = thing["timeInBed"]

                outfile.write(period+","+str(reportingDate)+","+str(start)+","+str(end)+","+str(asleepTime)+","+str(awakeTime)+","+str(awakeNumber)+","+str(restlessTime)+","+str(restlessNumber)+","+str(fallAsleep)+","+str(lieIn)+","+str(inBedTime)+"\n")
                print(asleepTime)

        reportingDate += datetime.timedelta(days=1)
        print("Done "+str(reportingDate))
    return()




writeData("YYYY-MM-DD start of apart period", "YYYY-MM-DD end of apart period", "Before")
writeData("YYYY-MM-DD start of together period", "YYYY-MM-DD end of together period", "After")

outfile.close()
