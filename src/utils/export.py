import os
from datetime import datetime
from fpdf import FPDF
from config import EXPORT_DIRECTORY
from utils import helpers

def generate_export_name(project_name, filetype):
    now = datetime.now()
    date = now.strftime('%Y%m%d')

    filename =f"{date}{project_name}.{filetype}"
    return filename

def generate_export_filepath(project_name, filetype):
    filename = generate_export_name(project_name, filetype)
    filepath = os.path.join(EXPORT_DIRECTORY,filename)
    return filepath

def generate_export_text_body(username, project_name, times, total_time):
    textbody = f"""Daily log of {username} on project {project_name}:\n"""
    for time in times:
        textbody += f"{time[0]}: {helpers.time_to_string(time[1])} \n"
    textbody += "__________________\n"
    textbody += f"Time in total: {total_time}"
    return textbody

def export_txt(textbody, filepath):
    with open(filepath, "w", encoding="utf8") as file:
        file.write(textbody)

def export_pdf(textbody, filepath):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, textbody)
    pdf.output(filepath, 'F').encode('latin-1')

def export(filetype, username, project_name, times, total_time):
    export_functions = {
            "txt": export_txt,
            "pdf": export_pdf
        }
    filename = generate_export_name(project_name, filetype)
    filepath = generate_export_filepath(project_name, filetype)
    textbody = generate_export_text_body(username, project_name, times, total_time)

    export_functions[filetype](textbody, filepath)

    return filename
