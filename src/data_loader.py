from pypdf import PdfReader
import os

def load_resume(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Resume not found at: {file_path}")

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text


def load_job_description(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JD not found at: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()