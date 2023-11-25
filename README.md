# extracao_palavras_chaves
Análise de palavras chave das estrategias nacionais de IA
Este script Python foi desenvolvido para ser executado no ambiente do Google Colab. Ele extrai e destaca palavras-chave específicas de um documento do Microsoft Word, facilitando a análise rápida de documentos para identificar trechos relevantes.

Funcionalidades
Extração de texto do Word: Utiliza a biblioteca docx2txt para extrair texto de arquivos .docx.
Destaque de palavras-chave: Busca e destaca palavras-chave predefinidas no documento.
Como Usar no Google Colab
Instalação da Biblioteca docx2txt:

No Colab, execute !pip install docx2txt para instalar a biblioteca necessária.
Upload do Arquivo Word:

No Google Colab, use a função de upload de arquivo para carregar o documento .docx que deseja analisar.
Configuração do Script:

Defina as palavras-chave desejadas na lista keywords.
Atualize o word_path para o caminho do arquivo após o upload.
Execução do Script:

Execute o script no Colab e observe os resultados com as palavras-chave destacadas.
Saída Esperada
O script imprimirá trechos do documento onde cada palavra-chave especificada é encontrada, com as palavras-chave destacadas em amarelo para facilitar a identificação.

