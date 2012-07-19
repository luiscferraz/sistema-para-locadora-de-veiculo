#-*- coding:utf-8 -*-
'''
Created on 19/07/2012

@author: 
'''
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica
import os


class Impressao(object):
        
    pdf = Canvas('././teste2.pdf', pagesize = letter) #Nome do arquivo e Tipo do papel
    pdf.setFont("Courier",12) #Seta a fonte para Courier tamanho 12
    pdf.setStrokeColorRGB(1, 0, 0)
    pdf.drawString(100, 750, "MEU PRIMEIRO PDF") #Escreve o texto na posição (0,0) = (x,y)
    pdf.showPage()
    pdf.save()
    
    os.system("teste2.pdf");
        

