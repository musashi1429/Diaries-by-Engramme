from docxtpl import DocxTemplate


template_values = {}
document = DocxTemplate("template.docx")
# Logique ici
document.render(template_values)
document.save("generated.docx")
