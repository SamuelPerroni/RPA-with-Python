from chrome import ChromeAuto as chrome

if __name__ == '__main__':
    site = r'https://cidades.ibge.gov.br/'
    caminhoPDF = r'Arquivos de entrada\Cidades.pdf'

    chrome = chrome()
    pdf = pdf()

    pdf.gera_txt(caminhoPDF)
    chrome.acessa(site)

