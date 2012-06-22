# -*- coding: utf8 -*-
from os import environ, path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm

"""
Generate grid paper PDF in A4 size. For kids drawing exercises.
Jun 2012 by Julián Romero <julian@wuonm.com>
"""
# configurable dimensions
topMargin = 0.5 * cm
bottomMargin = 0.5 * cm
leftMargin = 0.5 * cm
rightMargin = 0.5 * cm

gridScale = 5
smallGrid = 0.5 * cm
bigGrid = smallGrid * gridScale

# paper dimensions
paperWidth = A4[0]
paperHeight = A4[1]

# configuragle widths
marginLineWidth = 0.60
lineWidth = 1.0
sizeScale = 1.75 # top and bottom strips factor scale using writting strip as unit

HOME = environ["HOME"]
output = canvas.Canvas(path.join(HOME, "Desktop", "DrawingGrid-A4.pdf"))

light = colors.lightgrey
dark = colors.lightgrey
black = colors.darkgrey

# Debug / Origin is left,bottom
DEBUG = False
if DEBUG:
    output.setLineWidth(2)
    output.setStrokeColor(colors.red)
    output.line(0, 0, paperWidth/2, paperHeight/2)
    output.setLineWidth(2)
    output.setStrokeColor(colors.blue)
    output.line(0, paperHeight, paperWidth/2, paperHeight/2)

# vertical lines
s = int(paperWidth / smallGrid) 
x = paperWidth - (paperWidth - s * smallGrid) / 2;
n = 2
while x >= 0:
    if n > 0 and n % gridScale == 0:
        output.setStrokeColor(colors.darkgrey)
        output.setLineWidth(lineWidth)
    else:
        output.setStrokeColor(colors.lightgrey)
        output.setLineWidth(lineWidth / 2)
    output.line(x, 0, x, paperHeight)
    x = x - smallGrid
    n = n + 1

# horizontal lines
s = int(paperHeight / smallGrid) 
y = paperHeight - (paperHeight - s * smallGrid) / 2;
n = 3
while y >= 0:
    if n > 0 and n % gridScale == 0:
        output.setStrokeColor(colors.darkgrey)
        output.setLineWidth(lineWidth)
    else:
        output.setStrokeColor(colors.lightgrey)
        output.setLineWidth(lineWidth / 2)
    output.line(0, y, paperWidth, y)
    y = y - smallGrid
    n = n + 1

# write pdf
output.save()
