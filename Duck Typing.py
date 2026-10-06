class PDFReport:
    def send(self):
        print("Sending PDF Report")
class ExcelSheet:
    def send(self):
        print("Sending Excel Sheet")
class EmailMessage:
    def send(self):
        print("Sending Email Meassage")
def dispatch(item):
    item.send()
pdf=PDFReport()
excel=ExcelSheet()
email=EmailMessage()

dispatch(pdf)
dispatch(excel)
dispatch(email)
