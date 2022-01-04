import os
from static.reports import Model
import pandas as pd
from flask import Flask, render_template, request, flash, make_response, redirect, url_for
from werkzeug.utils import secure_filename

from static.reports.Report1 import Report1

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/resources"


##@app.route('/', methods=["POST"])
@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/cargarCSV', methods=['GET', 'POST'])
def cargarCSV():
    if (request.method == 'POST'):
        if request.files:
            fileCSV = request.files['openCSV']
            print(fileCSV.filename)
            filename = secure_filename(fileCSV.filename)
            fileCSV.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        ##COMENTADO PORQUE AUN NO SE COMO FUNCIONA ESTO DEL RESPONSE
        ##flash("Archivo Cargado Correctamente")
        response = make_response(redirect(url_for('typeReport')))
        response.set_cookie("name",fileCSV.filename)
    ##return "Archivo Subido Correctamente" + fileCSV.filename
    ##return render_template("index.html")
    return response

@app.route('/typeReport')
def typeReport():
    nameFile = request.cookies.get("name","Undefined")
    columns = []
    if(not (nameFile == "Undefined")):
        dataReader = pd.read_csv(app.config['UPLOAD_FOLDER'] + "/" + nameFile)
        columns = dataReader.columns;
    return render_template("typeReport.html", columns=columns)

@app.route('/typeReportSelected', methods = ['POST'])
def typeReportSelected():
    nameFile = request.cookies.get("name", "Undefined")
    typeReport = request.form.get("listadoReportes")
    columns = []
    if (not (nameFile == "Undefined")):
        dataReader = pd.read_csv(app.config['UPLOAD_FOLDER'] + "/" + nameFile)
        columns = dataReader.columns;
    if(typeReport == "reporte1"):
        return render_template("parametersReport1.html", columns=columns, typeReport=typeReport)
    elif(typeReport == "reporte2"):
        return render_template("parametersReport1.html", columns=columns, typeReport=typeReport)

@app.route('/parameters', methods = ['GET','POST'])
def parameters():
    nameFile = request.cookies.get("name", "Undefined")
    nameFile = app.config['UPLOAD_FOLDER'] + "/" + nameFile
    column = request.form.get("columnFilter")
    date = request.form.get("varX")
    infected = request.form.get("varY")
    country = request.form.get("filter")
    return generateReport1(column=column, date=date, infected=infected, country=country, file=nameFile)

def generateReport1(column, date, infected, country, file):
    report1 = Report1(filename=file, country = column, nameCountry=country, date = date, infected = infected)
    
    data = report1.generateReport()
    return render_template("resultReport.html", report=data, filename=app.config['UPLOAD_FOLDER'] + "/" + "report.png")


if __name__ == '__main__':
    app.run(debug=True)
    app.m
