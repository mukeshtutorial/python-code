def convertSec(timeseconds):
    secondValue = timeseconds % (24 * 3600)
    timeHour = secondValue // 3600
    secondValue %= 3600
    timeMinutes = secondValue // 60
    secondValue %= 60
    print("converting given time in seconds",
          timeseconds, "=", timeHour, "hrs", timeMinutes, "minutes")


# given time in seconds
timeseconds = 30000
# passing given time in seconds to convertSec function to convert it to minutes and hours
convertSec(timeseconds)