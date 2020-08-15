fileName = 'ESS_Diversity_Score.pdf'
documentTitle = 'ESS Diversity Score'
title = 'ESS Event Diversity Score'
position_title = '<ESS Position Here>'


#Create PDF file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors


import numpy as np
import math

#Function to label grid
def LabelGrid(pdf, width, height):
    pdf.setFont('Bebas', 10)
    x_grid = np.linspace(50,width - 50,10)
    y_grid = np.linspace(50,height - 50,12)


    for label in x_grid:
        label = int(math.ceil(label/10.0)*10)
        pdf.drawString(label, height*(32/33), ('x' + str(label)))

    for label in y_grid:
        label = int(math.ceil(label/10.0)*10)
        pdf.drawString(10, label, ('y' + str(label)))





pdfmetrics.registerFont(
    TTFont('Bebas', 'BebasNeue-Regular.ttf')
)



pdf = canvas.Canvas(fileName, pagesize= letter)
width, height = letter #keep for later

pdf.setFillColor(colors.firebrick)
pdf.setFont('Bebas', 28)
pdf.rect(0,height-70,300,70, stroke = 0, fill = 1)

#Draw Triangle (Turn into a function later)
triangle = pdf.beginPath()
triangle.moveTo(300, height-70)
triangle.lineTo(310, height)
triangle.lineTo(300, height)
pdf.drawPath(triangle, fill = 1, stroke = 0)

#Draw the text
pdf.setFillColor(colors.white)
pdf.setTitle(documentTitle)
pdf.drawString(35, height - 50, title)




#Draw Second Triangle (Turn into a function later)
pdf.setFillColor(colors.sandybrown)
triangle2 = pdf.beginPath()
triangle2.moveTo(230, height-100)
triangle2.lineTo(240, height-70)
triangle2.lineTo(230, height-70)
pdf.drawPath(triangle2, fill = 1, stroke = 0)

#Draw Second Rectangle (Make a damn function)
pdf.rect(0,height-100,230,30, stroke = 0, fill = 1)

#Draw the text
pdf.setFillColor(colors.white)
pdf.setFont('Bebas', 18)
pdf.drawString(35,height-90,position_title)

#Set image logo on top right
pdf.drawInlineImage('logo.png', 325, 715)

#Call Custom Label Grid Function
pdf.setFillColor(colors.black)
LabelGrid(pdf, width, height)






pdf.save()

