# Most of this is taken whole-cloth from "https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python"
def createBoxRental():
    
    

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # can.grid([x for x in range(700) if x % 20==0],[x for x in range(850) if x % 20==0])
    # can.grid([x+1 for x in range(700) if x % 100==0],[x+1 for x in range(850) if x % 100==0])

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
    weekendingDate = "January 21, 2023"

    # print(datetime.fromordinal(date.today().toordinal() + (5 - date.today().weekday())).strftime("%B %w, %Y"))

    thisSaturdayAsDatetime = date.fromordinal(date.today().toordinal() + (5 - date.today().weekday()))
    
    weekendingDateTimeFormat = thisSaturdayAsDatetime.strftime("%B %d, %Y")


    createBoxRental()