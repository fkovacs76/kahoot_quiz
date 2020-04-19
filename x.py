
#only python3, check args carefully (domains)

import xlsxwriter
import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument("--file",help="input file")
parser.add_argument("--timelimit", type=int, help="change time limit for all questions (5,10,20,30,60,120 seconds)" )
parser.add_argument("--length", type=int, help="number of questions" )
parser.add_argument("--domains",help="list of domains to choose from like Foldrajz,Kornyezet,Matek,Tortenelem")
args = parser.parse_args()

domains = args.domains.split(',')

with open(args.file, "r", encoding='utf16') as f:
 dict = {}
 l = []
 line = " "
 while line:
  line = f.readline()
  if not line.strip(): continue 
  dict['Mufaj'] = line.strip()
  dict['Kerdes'] = f.readline().strip()
  dict['Valasz1'] = f.readline().strip()
  dict['Valasz2'] = f.readline().strip()
  dict['Valasz3'] = f.readline().strip()
  dict['Valasz4'] = f.readline().strip()
  dict['Idokorlat'] = f.readline().strip()
  dict['HelyesValasz'] = f.readline().strip() 
  l.append(dict.copy())
  
print (len(l), "questions processed")  

filtered = [i for i in l if i['Mufaj'] in domains] 


cnt = 0
selected = []
while cnt < args.length:
  rnd = random.randint(0,len(filtered)-1)
  if rnd in selected: 
    continue
  selected.append(rnd)
  cnt += 1

selected_questions = [filtered[i] for i in selected]

workbook = xlsxwriter.Workbook('quiz.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,1,"Question - max 95 characters")
worksheet.write(0,2,"Answer 1 - max 60 characters")
worksheet.write(0,3,"Answer 2 - max 60 characters")
worksheet.write(0,4,"Answer 3 - max 60 characters")
worksheet.write(0,5,"Answer 4 - max 60 characters")
worksheet.write(0,6,"Time limit (sec) - 5,10,20,30,60,90 or 120 secs")
worksheet.write(0,7,"Correct answer(s) - choose at least one")

worksheet.set_column('A:A', 3)
worksheet.set_column('B:B', 90)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 15)
worksheet.set_column('G:G', 3)
worksheet.set_column('H:H', 3)

row = 1
for i in selected_questions:
  worksheet.write(row,0,row+1)
  worksheet.write(row,1,i['Kerdes'])
  worksheet.write(row,2,i['Valasz1'])
  worksheet.write(row,3,i['Valasz2'])
  worksheet.write(row,4,i['Valasz3'])
  worksheet.write(row,5,i['Valasz4'])
  if args.timelimit:
    worksheet.write(row,6,args.timelimit)
  else:
    worksheet.write(row,6,i['Idokorlat'])
  worksheet.write(row,7,i['HelyesValasz'])
  row +=1

workbook.close()
