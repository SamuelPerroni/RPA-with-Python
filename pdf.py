import PyPDF2

class PDFAuto:
    def __init__(self):
        pass

    def gera_txt(self, origemPDF):
        dados = []
        try:
            pdf_file = open(origemPDF, 'rb')
        except Exception as e:
            print(e)
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        for line in read_pdf:
            dados = dados.append(line)
        try:
            with open(r'Arquivos de entrada\cidades.txt', 'r') as arquivoTxt:
                arquivoTxt.write(dados)
            arquivoTxt.close()
        