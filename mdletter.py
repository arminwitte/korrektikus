# created with gemini

import fpdf
import markdown

def create_din5002_letter(template_file, recipient_address):
    """
    Erstellt einen Brief nach DIN 5002 aus einer Markdown-Vorlage.

    Args:
        template_file: Pfad zur Markdown-Vorlage.
        recipient_address: Empfängeradresse als String.
    """

    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)

    # Briefkopf (Platzhalter für deine eigenen Informationen)
    pdf.cell(w=0, h=10, txt='Dein Name', ln=1, align='C')
    pdf.cell(w=0, h=10, txt='Deine Adresse', ln=1, align='C')

    # Leerzeile
    pdf.cell(w=0, h=5, ln=1)

    # Datum
    pdf.cell(w=0, h=10, txt=pdf.date, ln=1, align='R')

    # Brieffenster
    pdf.cell(w=0, h=5, ln=1)
    pdf.cell(w=100, h=50, txt=recipient_address, border=1, ln=1)

    # Leerzeile
    pdf.cell(w=0, h=5, ln=1)

    # Briefinhalt aus der Markdown-Vorlage
    with open(template_file, 'r') as f:
        md_text = f.read()
    html = markdown.markdown(md_text)
    pdf.write_html(html)

    # Fußzeile (optional)
    pdf.cell(w=0, h=10, txt='Gruß', ln=1, align='C')

    pdf.output('brief.pdf')

# Beispielaufruf
template = 'brief_vorlage.md'
empfaenger = 'Max Mustermann\nMusterstraße 1\n12345 Musterstadt'
create_din5002_letter(template, empfaenger)
