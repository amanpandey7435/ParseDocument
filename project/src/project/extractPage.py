
from pypdf import PdfReader
from docx import Document
import re


def extract_pdf(uploaded_file):

    reader = PdfReader(uploaded_file)

    extracted_text = ""

    for page in reader.pages:

        text = page.extract_text()

        print("TEXT FROM PAGE:", text)

        if text:
            extracted_text += text + "\n"

    print("FINAL TEXT:", extracted_text)

    return split_sections(extracted_text)


def extract_docx(uploaded_file):

    document = Document(uploaded_file)

    extracted_text = ""

    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            print("DOCX TEXT:", repr(text))
            extracted_text += text + "\n"

    print("FINAL DOCX TEXT:")
    print(extracted_text)

    return split_sections(extracted_text)


def split_sections(text):

    if not text:
        return {}

    sections = {}

    current_heading = None
    current_content = []

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        if is_heading(line):

            if current_heading:
                sections[current_heading] = " ".join(current_content)

            current_heading = line
            current_content = []

        else:

            current_content.append(line)

    if current_heading:
        sections[current_heading] = " ".join(current_content)

    return sections


def is_heading(line):

    pattern = r"^(?:[A-Z]\.\d+|\d+(?:\.\d+)*)\s+.+$"

    return bool(re.match(pattern, line))
