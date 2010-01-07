# -*- coding: utf8 -*-
from os import environ, path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm

"""
Generate ruled paper PDF in A4 size. For kids handwriting exercises.
7th Jan 2010 by Julián Romero <julian@wuonm.com>
"""

# configurable dimensions
topMargin = 3.5 * cm
bottomMargin = 1.5 * cm
leftMargin = 2.5 * cm
size = 3.5 * mm # writting strip
separation = 1 * mm
titleMargin =  topMargin * 0.66

# configuragle widths
marginLineWidth = 0.60
lineWidth = 1.0
sizeScale = 1.75 # top and bottom strips factor scale using writting strip as unit

HOME = environ["HOME"]
outCanvas = canvas.Canvas(path.join(HOME, "Desktop", "Montessori-A4.pdf"))

light = colors.lightgrey
dark = colors.lightgrey
black = colors.darkgrey

# title, name, date
outCanvas.setLineWidth(lineWidth)
outCanvas.setStrokeColor(black)
outCanvas.line(leftMargin + 1 * cm, A4[1] - titleMargin, A4[0] - 1 * cm, A4[1] - titleMargin)

# left margin
outCanvas.setLineWidth(marginLineWidth)
outCanvas.setStrokeColor(black)
outCanvas.line(leftMargin, 0, leftMargin, A4[1])
outCanvas.setStrokeColor(dark)
outCanvas.line(leftMargin - marginLineWidth, 0, leftMargin - marginLineWidth, A4[1])

position = A4[1] - topMargin
while position >= bottomMargin:
    # upper line
    outCanvas.setLineWidth(lineWidth/2)
    outCanvas.setStrokeColor(light)
    outCanvas.line(0, position, A4[0], position)
    # low line
    outCanvas.setStrokeColor(dark)
    outCanvas.setLineWidth(lineWidth/2)
    outCanvas.line(0, position - (size * sizeScale), A4[0], position - (size * sizeScale))
    # base line light
    outCanvas.setStrokeColor(light)
    outCanvas.setLineWidth(lineWidth/2)
    outCanvas.line(0, position - (size + size * sizeScale) - lineWidth/2, A4[0], position - (size + size * sizeScale) - lineWidth/2)
    # base line dark
    outCanvas.setStrokeColor(black)
    outCanvas.setLineWidth(lineWidth/2)
    outCanvas.line(0, position - (size + size * sizeScale), A4[0], position - (size + size * sizeScale))
    # down line
    outCanvas.setStrokeColor(light)
    outCanvas.setLineWidth(lineWidth/2)
    outCanvas.line(0, position - (size + 2 * size * sizeScale), A4[0], position - (size + 2 * size * sizeScale))

    position = position - (size + 2 * size * sizeScale + separation)

# write pdf
outCanvas.save()
