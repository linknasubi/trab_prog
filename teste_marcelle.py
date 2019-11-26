import xml.dom.minidom as mnd
import pandas as pd
from pandas import ExcelWriter


def artigosPublicados(path, roo_t, child1, child2, *argv):
    doc = mnd.parse(path);
    contador = -1

    root = doc.getElementsByTagName(roo_t); #Pega o root dos currículos
    
    child_dadosBasicos = []; #Cria uma lista para o endereço de todas as child que serão inseridas aqui e na lista posterior
    child_detalhamento = [];

    atributos = [] #Cria uma lista para armazenar o atributo de todas child
    atributos_Tag = [] #Lista para armazenar a Tag dos atributos
    
    dic = {}#Dicionário que será retornado no final da função


    for i in root:

        child_dadosBasicos.append( i.getElementsByTagName(child1)) #Adiciona o endereço da respectiva child nas listas child_X

        child_detalhamento.append( i.getElementsByTagName(child2))
        
    for arg in argv:
        contador += 1 #Contador para alocar os atributos em seus devidos lugares
        atributos.append([]) #Cria uma sub-lista que irá armazenar os atributos de cada Tag separadamente
        atributos_Tag.append(arg) #Adiciona a Tag em questão na lista de Tag

        for i, j in zip (child_dadosBasicos, child_detalhamento):

            try:
                atributos[contador].append(i[0].attributes[arg].value) #Tenta buscar o atributo na primeira child, se não for encontrado parte para o segundo
            except KeyError:
                atributos[contador].append(j[0].attributes[arg].value)
    
    for i in range(len(atributos)):
        dic[atributos_Tag[i]] = (atributos[i]) #Adiciona para cada chave a tupla contendo todos elementos da sublista em questão
                                               
        
    contador = 0
    for j in range(len(atributos[0])): #Serve para a próxima função, uma vez que precisamos fazer uma iteração de todas linhas presentes no excel
        contador+=1
                
            
    return dic, contador

def excelMaker(dictionary):
    df = pd.DataFrame(dictionary[0]) #Cria o dataframe pelo pandas
    
    writer = ExcelWriter("Curriculo.xlsx") #Cria o arquivo excel
    
    workbook=writer.book #Cria a instância book para podermos utilizar a função
    
    formato = workbook.add_format({'text_wrap': True}) #Armazena o formato que buscamos, nesse caso de quebra de texto
    
    df.to_excel(writer, "Trabalho_Eventos", index=False) #É adicionado o nome do sheet e em seguida seleciona a opção de ter ou não index
    
    worksheet = writer.sheets['Trabalho_Eventos'] #Variável para identificar com qual sheet será trabalhado
    
    worksheet.set_column(0, dictionary[1], 20, formato) #É modificado o tamanho da coluna, selecionando de qual até qual coluna será modificado
    #No caso acima o último parâmetro passado se trata do formato de ter quebra de texto
    
    for i in range(dictionary[1]):
        
        worksheet.set_row(i,90, formato) #Diferente da definição da coluna, no set_row não existe parâmetro de início e fim para linha, apenas 
        #da linha em questão, por isso é necessário a iteração que se trata da variável contador da função anterior
        
    writer.save()
    writer.close() #Salva e finaliza a edição do arquivo
    

#Os 4 primeiros parâmetros se tratam do caminho do curriculo em questão, do nome da root, e o nome dos dois childs em que serão buscados
#os atributos, todos parâmetros após estes se trata dos atributos que desejamos inserir no excel.
curr_Analise = artigosPublicados("curriculo.xml","TRABALHO-EM-EVENTOS",'DADOS-BASICOS-DO-TRABALHO', 'DETALHAMENTO-DO-TRABALHO', 'TITULO-DO-TRABALHO', 'ANO-DO-TRABALHO',
                      'TITULO-DOS-ANAIS-OU-PROCEEDINGS', 'DOI', 'CIDADE-DO-EVENTO')


#Recebe a variável anterior para criação do excel
excel = excelMaker(curr_Analise)
