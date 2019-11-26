import xml.dom.minidom as mnd

# Segue as instruções de como utilizar a função
# Passe o caminho do arquivo como parâmetro
# Ele retornará uma lista de listas com cada artigo publicado
# 
# artigos[i][0] -> Retorna o título do artigo
# artigos[i][1] -> Retorna o ano do artigo
# artigos[i][2] -> Retorna o DOI do artigo
# artigos[i][3] -> Retorna o título do periódico 
#

def artigosPublicados(path = ''):
    doc = mnd.parse(path);

    # Pega o root dos artigos
    root = doc.getElementsByTagName("ARTIGOS-PUBLICADOS");

    child_dadosBasicos = [];
    child_detalhamentoArtigo = [];

    tituloArtigo = [];
    anoArtigo = [];
    DOIArtigo = [];

    tituloPeriodico = [];
    
    artigos = [];

    # Pra cada elemento em "ARTIGOS-PUBLICADOS"
    for i in root:
        # Nos dados básicos, procure: Título, Ano e o DOI
        child_dadosBasicos.append( i.getElementsByTagName("DADOS-BASICOS-DO-ARTIGO") );
        # No detalhamento do artigo, procure: Título do periódico
        child_detalhamentoArtigo.append( i.getElementsByTagName("DETALHAMENTO-DO-ARTIGO"));

    # Procure nos dados básicos do artigo: Título, Ano e o DOI
    for i in child_dadosBasicos:
        tituloArtigo.append( i[0].attributes["TITULO-DO-ARTIGO"].value );
        anoArtigo.append(i[0].attributes["ANO-DO-ARTIGO"].value); 
        DOIArtigo.append(i[0].attributes["DOI"].value);


    # Procure no detalhamento do artigo: Título do periódico
    for i in child_detalhamentoArtigo:
        tituloPeriodico.append(i[0].attributes["TITULO-DO-PERIODICO-OU-REVISTA"].value);

    # Para cada titulo de artigo, cria uma lista contendo todas as variáveis importantes e adicione à lista artigos
    for i in range(len(tituloArtigo)):
        artigo = [tituloArtigo[i], anoArtigo[i], DOIArtigo[i], tituloPeriodico[i]]
        artigos.append(artigo);
            
    return artigos;

caminhoDoXML = "curriculo.xml";
artigo = artigosPublicados(caminhoDoXML);




