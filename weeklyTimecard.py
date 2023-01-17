# Most of this is taken whole-cloth from "https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python"
def createBoxRental():
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from privateVariables import private_key


    weekendingDate = "January 21, 2023"


    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    can.grid([x for x in range(700) if x % 20==0],[x for x in range(850) if x % 20==0])
    can.drawString(10, 10, ". (10, 10)")
    can.drawString(100, 10, ". (100, 10)")
    can.drawString(150, 10, ". (150, 10)")
    can.drawString(200, 10, ". (200, 10)")
    can.drawString(250, 10, ". (250, 10)")
    can.drawString(300, 10, ". (300, 10)")
    can.drawString(350, 10, ". (350, 10)")
    can.drawString(400, 10, ". (400, 10)")
    can.drawString(450, 10, ". (450, 10)")
    can.drawString(500, 10, ". (500, 10)")
    can.drawString(550, 10, ". (550, 10)")
    can.drawString(600, 10, ". (600, 10)")

    can.drawString(100, 100, ". (100, 100)")

    # Location for Employee name
    can.drawString(135, 645, "Throsby Wells")
    # Location for special string
    can.drawString(425, 645, private_key)


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
    createBoxRental()