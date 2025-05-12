from bs4 import BeautifulSoup

def extrair_dados_processo(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Classe Judicial
    classe_div = soup.select_one("span#j_id151\\:processoTrfViewView\\:j_id180 div.value.col-sm-12")
    classe = classe_div.text.strip() if classe_div else ""

    # Assunto
    assunto_div = soup.select_one("span#j_id151\\:processoTrfViewView\\:j_id191 div.value.col-sm-12 > div.col-sm-12")
    assunto = assunto_div.text.strip() if assunto_div else ""

    # Vara
    vara_div = soup.find("b", string="Órgão Julgador")
    vara = ""
    if vara_div and vara_div.next_sibling:
        vara = vara_div.next_sibling.strip()

    # Partes (simplificado para exemplo)
    partes = []
    for parte in soup.select("table.rich-table tbody tr td span"):
        texto = parte.text.strip()
        if texto:
            partes.append(texto)

    return {
        "classe": classe,
        "assunto": assunto,
        "vara": vara,
        "partes": partes
    }

def extrair_andamentos(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    painel_eventos = soup.find('div', {'id': 'j_id151:processoEventoPanel_body'})
    if not painel_eventos:
        return []

    tabela = painel_eventos.find('table', {'class': 'rich-table'})
    andamentos = []

    if tabela:
        linhas = tabela.find_all('tr')
        for linha in linhas[1:]:  # pular cabeçalho
            colunas = linha.find_all('td')
            if len(colunas) >= 2:
                movimento = colunas[0].get_text(strip=True)
                documento = colunas[1].get_text(strip=True)
                andamentos.append({
                    'movimento': movimento,
                    'documento': documento
                })

    return andamentos
