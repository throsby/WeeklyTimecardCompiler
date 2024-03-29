# The strategy of making a watermark to mask over the original pdf is taken whole-cloth from "https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python"
import os
try:
    os.environ['CONDA_DEFAULT_ENV']
except KeyError:
    print("\n\n  >>  You're not using the correct virtual envrionment. Throsby, if you're running this on your desktop, please run 'conda activate base' to run this application properly.\n\n")


from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# If you want my SSN steal it from me in person
from privateVariables import private_key
from datetime import datetime, date, timedelta, time

import pprint
import json

# Create a value that is always the coming Saturday
thisSaturdayAsDatetime = date.fromordinal(date.today().toordinal() + (5 - date.today().weekday()))

boxrentalFilenameString = ""
timecardFilenameString = ""

# Formats this Saturday as "Month DD, YYYY"
weekendingDate = thisSaturdayAsDatetime.strftime("%B %d, %Y")

sundayHours = 12
mondayHours = 12
tuesdayHours = 12
wednesdayHours = 12
thursdayHours = 12
fridayHours = 12
saturdayHours = 0

# For clearer code to fix in a month or so, these are the datetimes of the week, as Datetimes
sundayAsDatetime = thisSaturdayAsDatetime - timedelta(days=6)
mondayAsDatetime = thisSaturdayAsDatetime - timedelta(days=5)
tuesdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=4)
wednesdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=3)
thursdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=2)
fridayAsDatetime = thisSaturdayAsDatetime - timedelta(days=1)
saturdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=0)

# For clearer code to fix in a month or so, these are the dates of the week, as ints
sunday = thisSaturdayAsDatetime.day - 6
monday = thisSaturdayAsDatetime.day - 5
tuesday = thisSaturdayAsDatetime.day - 4
wednesday = thisSaturdayAsDatetime.day - 3
thursday = thisSaturdayAsDatetime.day - 2    
friday = thisSaturdayAsDatetime.day - 1
saturday = thisSaturdayAsDatetime.day - 0

workWeekAsDict = {
    "{}".format(sundayAsDatetime): {
        "Datetime": "{}".format(sundayAsDatetime),
        "day_of_the_week": "Sunday",
        "hours": 12
    },
    "{}".format(mondayAsDatetime): {
        "Datetime": "{}".format(mondayAsDatetime),
        "day_of_the_week": "Monday",
        "hours": 12
    },
    "{}".format(tuesdayAsDatetime): {
        "Datetime": "{}".format(tuesdayAsDatetime),
        "day_of_the_week": "Tuesday",
        "hours": 12
    },
    "{}".format(wednesdayAsDatetime): {
        "Datetime": "{}".format(wednesdayAsDatetime),
        "day_of_the_week": "Wednesday",
        "hours": 12
    },
    "{}".format(thursdayAsDatetime): {
        "Datetime": "{}".format(thursdayAsDatetime),
        "day_of_the_week": "Thursday",
        "hours": 12
    },
    "{}".format(fridayAsDatetime): {
        "Datetime": "{}".format(fridayAsDatetime),
        "day_of_the_week": "Friday",
        "hours": 12
    },
    "{}".format(saturdayAsDatetime): {
        "Datetime": "{}".format(saturdayAsDatetime),
        "day_of_the_week": "Saturday",
        "hours": 0
    }
}


workWeekAsJson = json.dumps(workWeekAsDict)


pprint.pprint(workWeekAsJson)
print("\n",workWeekAsJson,"\n")

with open("./workdatescalendar.json","w") as outfile:
    outfile.write(workWeekAsJson)


# print(workWeekAsDict.get("{}".format(sundayAsDatetime)))


weeklyHoursAsDateTime = [(sundayHours, sundayAsDatetime), (mondayHours, mondayAsDatetime), (tuesdayHours, tuesdayAsDatetime), (wednesdayHours, wednesdayAsDatetime), (thursdayHours, thursdayAsDatetime), (fridayHours, fridayAsDatetime), (saturdayHours, saturdayAsDatetime)]
# print(workWeekAsJson)
# weeklyHoursAsDateTimeAsJson = [(sundayHoursAsJson, sundayAsDatetime), (mondayHoursAsJson, mondayAsDatetime), (tuesdayHoursAsJson, tuesdayAsDatetime), (wednesdayHoursAsJson, wednesdayAsDatetime), (thursdayHoursAsJson, thursdayAsDatetime), (fridayHoursAsJson, fridayAsDatetime), (saturdayHoursAsJson, saturdayAsDatetime)]

def createBoxRental():
    print("Creating Box Rental for {}".format(weekendingDate))
    global boxrentalFilenameString
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # Location for Employee name
    can.drawString(135, 645, "Throsby Wells")
    # Location for special string
    can.drawString(425, 645, private_key)

    # Location for the weekly box rental rate
    can.drawString(150, 568, "$15/day")

    # Location for signature date
    can.drawString(360, 175, weekendingDate)

    # Location for Week ending date
    can.drawString(175, 530, weekendingDate)
    can.save()

    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # read your existing PDF
    existing_pdf = PdfReader(open(r"/Users/throsbywells/Desktop/Kanan Season 3 Box Rental Forms/S3 Box Rental w:e 000000.pdf", "rb"))
    output = PdfWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    # finally, write "output" to a real file
    boxrentalFilenameString = r"/Users/throsbywells/Desktop/Kanan Season 3 Box Rental Forms/S3 Box Rental w:e {0}-{1}-{2}.pdf".format(thisSaturdayAsDatetime.year,thisSaturdayAsDatetime.month,thisSaturdayAsDatetime.day)
    # print(boxrentalFilenameString)
    outputStream = open(boxrentalFilenameString, "wb")
    output.write(outputStream)
    outputStream.close()

def createTimeCard():
    global timecardFilenameString
    print("Creating TimeCard for {}".format(weekendingDate))
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # can.grid([x for x in range(801) if x % 25==0],[x for x in range(801) if x % 25==0])
    # can.grid([x+1 for x in range(801) if x % 100==0],[x+1 for x in range(801) if x % 100==0])

    # Location of name
    can.drawString(30, 505, "Throsby Wells")

    # Location of private key
    can.drawString(290, 505, private_key)

    # Location of guaranteed hours
    can.drawString(455, 530, "12")

    # Location of guaranteed rate
    can.drawString(525, 530, "21.42/hour")

    # Location of weekending
    can.drawString(615, 530, weekendingDate)

    # Location of job title
    can.drawString(455, 505, "HS Coordinator")
    
    # Location of meal allowance
    can.drawString(90, 192, "$15/day")

    daysOfWeekWorked = 0
    for pair in weeklyHoursAsDateTime:
        if (pair[0] != 0):
            # Creates the different lines for times and dates
            can.setFontSize(12)
            can.drawString(23, 430 - daysOfWeekWorked, "NY   NY")
            can.setFontSize(10)
            can.drawString(120, 430 - daysOfWeekWorked, "{0}/{1}/{2}".format(pair[1].month, pair[1].day, pair[1].year))
            # The endtime of work. Starting at 1:30PM to make lunch easier - adds the time worked for the respective day as time delta and combines the day worked with the hours worked
            endOfWorkAsDatetime = datetime.combine(pair[1], time(13, 30)) + timedelta(seconds=pair[0]*60*60)
            # print(datetime.strftime(endOfWorkAsDatetime, "%-H:%M%p"))

            can.drawString(191, 430 - daysOfWeekWorked, "1P     7P    7:30  {hours}".format(hours=datetime.strftime(endOfWorkAsDatetime, "%-H:%M%p")))
            daysOfWeekWorked = daysOfWeekWorked + 23

    can.save()

    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)

    # read your existing PDF
    existing_pdf = PdfReader(open(r"/Users/throsbywells/Desktop/TimeCards/BlankTimeCard.pdf", "rb"))
    output = PdfWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    # finally, write "output" to a real file
    timecardFilenameString = datetime.strftime(thisSaturdayAsDatetime, "/Users/throsbywells/Desktop/TimeCards/Timecard_-_Throsby_Wells_-_x%-m-%d-%Y.pdf")
    outputStream = open(timecardFilenameString, "wb")
    output.write(outputStream)
    outputStream.close()

# def createTimeCard(workWeekAsJson):
#     global timecardFilenameString
#     print("Creating TimeCard for {}".format(weekendingDate))
#     packet = io.BytesIO()
#     can = canvas.Canvas(packet, pagesize=letter)

#     # Location of name
#     can.drawString(30, 505, "Throsby Wells")
#     # Location of private key
#     can.drawString(290, 505, private_key)
#     # Location of guaranteed hours
#     can.drawString(455, 530, "12")
#     # Location of guaranteed rate
#     can.drawString(525, 530, "21.42/hour")
#     # Location of weekending
#     can.drawString(615, 530, weekendingDate)
#     # Location of job title
#     can.drawString(455, 505, "HS Coordinator")
#     # Location of meal allowance
#     can.drawString(90, 192, "$15/day")


#     daysOfWeekWorked = 0
#     for pair in weeklyHoursAsDateTime:
#         if (pair[0] != 0):
#             # Creates the different lines for times and dates
#             can.setFontSize(12)
#             can.drawString(23, 430 - daysOfWeekWorked, "NY   NY")
#             can.setFontSize(10)
#             can.drawString(120, 430 - daysOfWeekWorked, "{0}/{1}/{2}".format(pair[1].month, pair[1].day, pair[1].year))
#             # The endtime of work. Starting at 1:30PM to make lunch easier - adds the time worked for the respective day as time delta and combines the day worked with the hours worked
#             endOfWorkAsDatetime = datetime.combine(pair[1], time(13, 30)) + timedelta(seconds=pair[0]*60*60)
#             # print(datetime.strftime(endOfWorkAsDatetime, "%-H:%M%p"))

#             can.drawString(191, 430 - daysOfWeekWorked, "1P     7P    7:30  {hours}".format(hours=datetime.strftime(endOfWorkAsDatetime, "%-H:%M%p")))
#             daysOfWeekWorked = daysOfWeekWorked + 23

#     can.save()

#     # create a new PDF with Reportlab
#     new_pdf = PdfReader(packet)

#     # read your existing PDF
#     existing_pdf = PdfReader(open(r"/Users/throsbywells/Desktop/TimeCards/BlankTimeCard.pdf", "rb"))
#     output = PdfWriter()
#     # add the "watermark" (which is the new pdf) on the existing page
#     page = existing_pdf.pages[0])
#     page.merge_page(new_pdf.pages[0]))
#     output.add_page(page)

#     # finally, write "output" to a real file
#     timecardFilenameString = datetime.strftime(thisSaturdayAsDatetime, "/Users/throsbywells/Desktop/TimeCards/Timecard_-_Throsby_Wells_-_x%-m-%d-%Y.pdf")
#     outputStream = open(timecardFilenameString, "wb")
#     output.write(outputStream)
#     outputStream.close()


def mergeTCBR():
    output = PdfWriter()
    timecard = PdfReader(open(timecardFilenameString,"rb"))
    boxrental = PdfReader(open(boxrentalFilenameString,"rb"))

    timecardPage = timecard.pages[0]
    boxrentalPage = boxrental.pages[0]

    # page.merge_page(timecard.pages[0])
    output.add_page(boxrentalPage)
    output.add_page(timecardPage)
    outputStream = open(r"/Users/throsbywells/Desktop/MergedTCBR-PDFs/Throsby-Wells-w:e-{0}-{1}-{2} Combo.pdf".format(thisSaturdayAsDatetime.year,thisSaturdayAsDatetime.month,thisSaturdayAsDatetime.day), "wb")
    output.write(outputStream)
    outputStream.close()
    print("Merging files done!")

if __name__ == "__main__":
    createTimeCard()
    # createTimeCard(workWeekAsJson)
    createBoxRental()
    mergeTCBR()
    print("done!")