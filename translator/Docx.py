__author__ = 'dor'


from docx import Document
from docx.shared import Inches
from .models import Paper,Paragraph,Translated_Paragraph
import RegexTxt
from django.utils.encoding import smart_unicode


def WriteDocx(paper):
    document = Document()

    document.add_heading(paper.name+" - "+paper.code, 0)

    Paras=Paragraph.objects.filter(paperId=paper)
    for para in Paras:
        if(Translated_Paragraph.objects.filter(paraId=para).exists()):
            translate=Translated_Paragraph.objects.filter(paraId=para)[0].txt
        else:
            translate=RegexTxt.RepleceTxt(para.txt)
        p = document.add_paragraph(translate)
    # p.add_run('bold').bold = True
    # p.add_run(' and some ')
    # p.add_run('italic.').italic = True

    #     document.add_heading('Heading, level 1', level=1)
    #     document.add_paragraph('Intense quote', style='IntenseQuote')
    #
    # document.add_paragraph(
    #     'first item in unordered list', style='ListBullet'
    # )
    # document.add_paragraph(
    #     'first item in ordered list', style='ListNumber'
    # )
    #
    # document.add_picture('monty-truth.png', width=Inches(1.25))
    #
    # table = document.add_table(rows=1, cols=3)
    # hdr_cells = table.rows[0].cells
    # hdr_cells[0].text = 'Qty'
    # hdr_cells[1].text = 'Id'
    # hdr_cells[2].text = 'Desc'
    # for item in recordset:
    #     row_cells = table.add_row().cells
    #     row_cells[0].text = str(item.qty)
    #     row_cells[1].text = str(item.id)
    #     row_cells[2].text = item.desc

    # document.add_page_break()

    return document