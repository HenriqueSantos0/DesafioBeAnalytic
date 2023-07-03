# DesafioBeAnalytic
O Objetivo desse documento é descrever como foi o processo de resolução do desafio passado pela BeAnlatycis como parte do processo seletivo para a vaga de engenheiro de dados Jr.
As condições do desafio era as seguintes:
- Realizar a extração das informações da base de dados da [SteamDB](https://steamdb.info/sales/)
- Armazenar os Dados no Google Big Query
- Exportar ou conectar os dados com o Google Sheets
- Enviar o link do Google Sheets
## Ideias inciais
Para resolver esse problema eu pensei inicialmente em criar a arquitetura abaixo:
![Captura de tela de 2023-07-03 13-33-46](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/bb7fcc96-6eab-46f1-aa5e-60d57429493c)

###### *Essa arquitetura foi construida com o auxilio do [Excalidraw](https://excalidraw.com/#json=LHona4siCKr7fdWN9eZ0R,YQ31RtQY-k46EifE-siSDw).*

O objetivo era construir um código em python, e implementa-lo no Google Cloud Function, que realizasse a raspagem da pagina e salvasse essas informações no Google Cloud Storage, então estando o Google Cloud Storage na Mesma Região de uma base de dados no Big Query, transferir os arquivos e por ultimo conectar esse dados ao Google Sheets.
