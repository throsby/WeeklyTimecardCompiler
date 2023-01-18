# Most of this is taken whole-cloth from "https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python"
def createBoxRental():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    can.grid([x for x in range(700) if x % 20==0],[x for x in range(850) if x % 20==0])
    can.grid([x+1 for x in range(700) if x % 100==0],[x+1 for x in range(850) if x % 100==0])

    # Location for Employee name
    can.drawString(135, 645, "Throsby Wells")
    # Location for special string
    can.drawString(425, 645, private_key)

    # Location for the weekly box rental rate
    can.drawString(150, 568, "$15/week")

    # Location for signature date
    can.drawString(360, 175, weekendingDate)

    # Location for Week ending date
    can.drawString(175, 530, weekendingDate)
    can.save()

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(r"/Users/throsbywells/Desktop/Kanan Season 3 Box Rental Forms/S3 Box Rental w:e 000000.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    boxrentalFilenameString = r"/Users/throsbywells/Desktop/Kanan Season 3 Box Rental Forms/S3 Box Rental w:e {0}-{1}-{2}.pdf".format(thisSaturdayAsDatetime.year,thisSaturdayAsDatetime.month,thisSaturdayAsDatetime.day)
    # print(boxrentalFilenameString)
    outputStream = open(boxrentalFilenameString, "wb")
    output.write(outputStream)
    outputStream.close()

def createTimeCard():
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
    


    # Creates the different lines for times and dates
    daysOfWeekWorked = 0
    for pair in weeklyHoursAsDateTime:
        print("The pair: ", pair)
        if (pair[0] != 0):
            can.setFontSize(12)
            can.drawString(23, 430 - daysOfWeekWorked, "NY   NY")
            can.setFontSize(10)
            can.drawString(120, 430 - daysOfWeekWorked, "{0}/{1}/{2}".format(pair[1].month, pair[1].day, pair[1].year))
            can.drawString(195, 430 - daysOfWeekWorked, "{}".format(pair[0]))
            daysOfWeekWorked = daysOfWeekWorked + 23    


    can.drawString(90, 192, "$15/day")

    can.save()

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)

    # read your existing PDF
    existing_pdf = PdfFileReader(open(r"/Users/throsbywells/Desktop/TimeCards/BlankTimeCard.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # finally, write "output" to a real file
    # timecardFilenameString = r"/Users/throsbywells/Desktop/Kanan Season 3 Box Rental Forms/S3 Box Rental w:e {0}-{1}-{2}.pdf".format(thisSaturdayAsDatetime.year,thisSaturdayAsDatetime.month,thisSaturdayAsDatetime.day)
    # print(timecardFilenameString)
    outputStream = open("destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == "__main__":
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from privateVariables import private_key
    from datetime import date, timedelta

    # Create a value that is always the coming Saturday
    thisSaturdayAsDatetime = date.fromordinal(date.today().toordinal() + (5 - date.today().weekday()))
    
    # Formats this Saturday as "Month DD, YYYY"
    weekendingDate = thisSaturdayAsDatetime.strftime("%B %d, %Y")

    sundayHours = 12
    mondayHours = 12
    tuesdayHours = 12
    wednesdayHours = 12
    thursdayHours = 12
    fridayHours = 12
    saturdayHours = 0
    
    sundayAsDatetime = thisSaturdayAsDatetime - timedelta(days=6)
    mondayAsDatetime = thisSaturdayAsDatetime - timedelta(days=5)
    tuesdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=4)
    wednesdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=3)
    thursdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=2)
    fridayAsDatetime = thisSaturdayAsDatetime - timedelta(days=1)
    saturdayAsDatetime = thisSaturdayAsDatetime - timedelta(days=0)

    sunday = thisSaturdayAsDatetime.day - 6
    monday = thisSaturdayAsDatetime.day - 5
    tuesday = thisSaturdayAsDatetime.day - 4
    wednesday = thisSaturdayAsDatetime.day - 3
    thursday = thisSaturdayAsDatetime.day - 2    
    friday = thisSaturdayAsDatetime.day - 1
    saturday = thisSaturdayAsDatetime.day - 0

    weeklyHoursAsDateTime = [(sundayHours, sundayAsDatetime), (mondayHours, mondayAsDatetime), (tuesdayHours, tuesdayAsDatetime), (wednesdayHours, wednesdayAsDatetime), (thursdayHours, thursdayAsDatetime), (fridayHours, fridayAsDatetime), (saturdayHours, saturdayAsDatetime)]

    # print(weeklyHoursAsDateTime)

    createTimeCard()
    # createBoxRental()