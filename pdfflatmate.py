import webbrowser
from fileinput import filename

from click import style
from fpdf import FPDF

class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period= period

class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        total_days = self.days_in_house + flatmate2.days_in_house
        weight = self.days_in_house / total_days

        to_pay = weight * bill.amount
        return to_pay

class PDFreport:
    def __init__(self,filename):
        self.filename = filename

    def generate (self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill,flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill,flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format = "A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Bill", border=1, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)

amount = float(input("Enter the amount:"))
period = input("What is the bill period? Eg:Dec 23, 2020:")

the_bill = Bill(amount, period)

name1 = input("What is the first person's name?:")
days_in_house1 = int(input(f"How many days did {name1} had money during the period?:"))

name2 = input("What is the second person's name?:")
days_in_house2 = int(input(f"How many days did {name2} had money during the period?:"))

flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays:", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays:", flatmate2.pays(the_bill, flatmate1))

pdfreport = PDFreport(filename=f"{the_bill.period}.pdf")
pdfreport.generate(flatmate1, flatmate2, the_bill)