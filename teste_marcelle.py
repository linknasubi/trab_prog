import xml.dom.minidom as mnd
import pandas as pd
from pandas import ExcelWriter


doc = mnd.parse("curriculo.xml")
teste = doc.getElementsByTagName("TRABALHO-EM-EVENTOS")
childs1 = []
childs2 = []
tit = []
ano = []
tit_cnf = []
doi = []
dic = {}
contador = 0


#print(teste)
for i in teste:
    child1 = i.getElementsByTagName('DADOS-BASICOS-DO-TRABALHO')
    child2 = i.getElementsByTagName('DETALHAMENTO-DO-TRABALHO')
    childs1.append(child1)
    childs2.append(child2)
    

for i in childs1:
    tit.append(i[0].attributes['TITULO-DO-TRABALHO'].value)
    ano.append(i[0].attributes['ANO-DO-TRABALHO'].value)
    doi.append(i[0].attributes['DOI'].value)
    
for i in childs2:
    tit_cnf.append(i[0].attributes['TITULO-DOS-ANAIS-OU-PROCEEDINGS'].value)
    
for i,j,k,l in zip (tit,ano,tit_cnf,doi):
    contador += 1
    dic[str(j)] = {"Title":str(i), "Conference Title":str(k), "DOI": str(l)}
    

df = pd.DataFrame(dic)
writer = ExcelWriter("Teste_10.xlsx")
workbook=writer.book
formato = workbook.add_format({'text_wrap': True})
df.to_excel(writer, "Sheet1", index=True)
worksheet = writer.sheets['Sheet1']
worksheet.set_column(0, contador, 20, formato)
for i in range(contador):
    worksheet.set_row(i,90)
writer.save()
writer.close()

