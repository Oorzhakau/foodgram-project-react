from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.http import FileResponse

from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from typing import List, Dict
import io
import os

FONTS_ROOT = os.path.dirname(os.path.abspath(__file__))


def addTitle(doc: List, title: str, size: int, space: int, ta: int):
    doc.append(Spacer(1, 20))
    doc.append(Paragraph(title,
                         ParagraphStyle(
                             name='name',
                             fontName='RobotoFlex-Regular',
                             fontSize=size,
                             alignment=ta
                         )
                         )
               )
    doc.append(Spacer(1, space))
    return doc


def addParagraphs(doc: List, text: str, size: int):
    for line in text:
        doc.append(Paragraph(line,
                             ParagraphStyle(
                                 name='line',
                                 fontName='RobotoFlex-Regular',
                                 fontSize=size,
                                 alignment=TA_LEFT
                             )
                             )
                   )
        doc.append(Spacer(1, 12))
    return doc


def create_pdf(obj: Dict[str, str]):
    buffer = io.BytesIO()

    font_fullpath = os.path.join(FONTS_ROOT, 'fonts/', 'RobotoFlex-Regular.ttf')
    pdfmetrics.registerFont(TTFont('RobotoFlex-Regular', font_fullpath))

    doc = addTitle([], obj['doc_title'], 24, 24, TA_CENTER)
    doc = addTitle(doc, obj['title'], 18, 12, TA_CENTER)
    doc = addTitle(doc, obj['user'], 12, 12, TA_LEFT)
    pdf = SimpleDocTemplate(buffer,
                            pagesize=A4,
                            rightMargin=12,
                            leftMargin=12,
                            topMargin=12,
                            bottomMargin=12)
    pdf.build(addParagraphs(doc, obj['text'], 12))
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=obj['file_name'])
