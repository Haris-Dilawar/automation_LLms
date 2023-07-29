from docx import Document

def read_word_document(file_path):
    doc = Document(file_path)

    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)

    return '\n'.join(full_text)