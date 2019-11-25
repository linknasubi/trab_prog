import xml.dom.minidom as mnd

doc = mnd.parse("curriculo.xml")
teste = doc.getElementsByTagName("TRABALHO-EM-EVENTOS")
childs1 = []
childs2 = []
tit = []
ano = []
tit_cnf = []
doi = []
dic = {}

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
    
    dic[str(i)] =  ("Year:"+str(j),"Conference Title:"+str(k),"Doi:"+str(l))
           
#{str(i) +":", ("Year:"+str(j),"Conference Title:"+str(k),"Doi:"+str(l))}
print(dic)