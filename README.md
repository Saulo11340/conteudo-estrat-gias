# extracao_palavras_chaves
Análise de palavras chave das estrategias nacionais de IA
Este script Python é projetado para extrair e destacar palavras-chave específicas de um documento do Microsoft Word. Ele é útil para análises rápidas de documentos, permitindo identificar e visualizar rapidamente os trechos relevantes que contêm palavras-chave predefinidas.

Funcionalidades
Extração de texto: O script usa a biblioteca docx2txt para extrair o texto de um arquivo .docx.
Destaque de palavras-chave: As palavras-chave especificadas são buscadas no texto, e os trechos que as contêm são destacados.
Como Usar
Instalação da Biblioteca Necessária:

Antes de executar o script, é necessário instalar a biblioteca docx2txt. Isso pode ser feito através do comando pip install docx2txt.
Definição de Palavras-chave:

Modifique a lista keywords no script para incluir as palavras-chave que deseja buscar no documento.
Especificar o Caminho do Arquivo Word:

Altere o valor de word_path para o caminho do seu arquivo .docx que deseja analisar.
Execução do Script:

Execute o script em um ambiente que suporte Python, como o Jupyter Notebook, para ver os resultados.
Exemplo de Saída
O script irá imprimir trechos do documento onde as palavras-chave são encontradas. Cada palavra-chave encontrada será destacada em amarelo para fácil identificação.
