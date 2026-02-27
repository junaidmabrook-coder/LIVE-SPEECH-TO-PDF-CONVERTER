from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import datetime
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    text = request.form.get("text")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Live Speech to PDF Output", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", size=11)
    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.ln(5)
    pdf.set_font("Arial", size=9)
    pdf.cell(0, 10, f"Generated on: {datetime.datetime.now()}", ln=True)

    file_name = "speech_to_pdf.pdf"
    pdf.output(file_name)

    return send_file(file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
