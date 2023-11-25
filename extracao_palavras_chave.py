import docx2txt
from IPython.display import HTML

# Define as palavras-chave a serem buscadas no documento
keywords = ['colaboração', 'cooperação', 'parceria', 'inovação aberta', 'rede', 'acordo', 'startup', 'ecossistema', 'aliança', 'hub de inovação', 'cluster tecnológico', 'conexões', 'transferência de tecnologia', 'inovação colaborativ', 'sinergia', 'intercâmbio', 'incubadora de empresas', 'aceleradora de startups', 'inovação tecnológica', 'pesquisa e desenvolvimento', 'P&D', 'em conjunto', 'conjunt', 'compartilhad', 'co-desenvolvimento', 'co-criação']

# Define o caminho para o arquivo Word
word_path = '/content/Estratégia da União Europeia.docx'

# Extrai o texto do arquivo Word
text = docx2txt.process(word_path)

# Busca pelas palavras-chave e imprime os trechos do texto em que elas aparecem
for keyword in keywords:
    if keyword in text:
        print(f"Trecho com a palavra-chave '{keyword}':")
        print("-------------------------------------")
        for paragraph in text.split('\n\n'):
            if keyword in paragraph:
                highlighted_paragraph = paragraph.replace(keyword, f'<mark style="background-color: yellow;">{keyword}</mark>')
                display(HTML(highlighted_paragraph))
        print("\n")
