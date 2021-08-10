from flask import Flask, render_template, request
from openpyxl import load_workbook, Workbook


excel = load_workbook('report.xlsx')

page = excel['Sheet']

app = Flask(__name__)

@app.route('/')
def homepage():
	txt = []
	print(len(page['A']))
	for i in range(1,len(page['A'])+1):
		txt.append(page["A"+str(i)].value)
	return render_template('index.html', goods=txt)
	

@app.route('/add/', methods=['POST'])
def add():
	good = request.form['good']
	page['A'+str(len(page['A'])+1)] = good
	excel.save('report.xlsx')
	return """ 
		<h1> Инвентарь пополнен" </h1>
		<a href='/'> Домой </a>
	"""