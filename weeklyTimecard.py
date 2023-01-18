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

    can.grid([x for x in range(801) if x % 25==0],[x for x in range(801) if x % 25==0])
    can.grid([x+1 for x in range(801) if x % 100==0],[x+1 for x in range(801) if x % 100==0])

    # Location of name
    can.drawString(30, 505, "Throsby Wells")

    # Location of private key
    can.drawString(290, 505, private_key)

    # Location of guaranteed hours
    can.drawString(455, 530, "12")

    # Location of guaranteed rate
    can.drawString(525, 530, "22.41/hour")

    # Location of weekending
    can.drawString(615, 530, weekendingDate)

    # Location of job title
    can.drawString(455, 505, "HS Coordinator")
    
    can.drawString(24, 430, "NY   NY")
    can.drawString(24, 405, "NY   NY")
    can.drawString(24, 385, "NY   NY")
    can.drawString(24, 360, "NY   NY")
    can.drawString(24, 335, "NY   NY")
    can.drawString(24, 312, "NY   NY")

    can.drawString(120, 430, "{0}/{1}/{2}".format(thisSaturdayAsDatetime.month, thisSaturdayAsDatetime.day, thisSaturdayAsDatetime.year))
    can.drawString(120, 405, "NY")
    can.drawString(120, 385, "NY")
    can.drawString(120, 360, "NY")
    can.drawString(120, 335, "NY")
    can.drawString(120, 312, "NY")


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
    from datetime import date

    # Create a value that is always the coming Saturday
    thisSaturdayAsDatetime = date.fromordinal(date.today().toordinal() + (5 - date.today().weekday()))
    
    weekendingDate = thisSaturdayAsDatetime.strftime("%B %d, %Y")

    sundayHours = 12
    mondayHours = 12
    tuesdayHours = 12
    wednesdayHours = 12
    thursdayHours = 12
    fridayHours = 12
    saturdayHours = 0
    
    weeklyHours = [sundayHours, mondayHours, tuesdayHours, wednesdayHours, thursdayHours, fridayHours, saturdayHours]


    createTimeCard()
    # createBoxRental()