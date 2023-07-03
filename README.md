# DesafioBeAnalytic
O Objetivo desse documento é descrever como foi o processo de resolução do desafio passado pela BeAnlatycis como parte do processo seletivo para a vaga de engenheiro de dados Jr.
As condições do desafio era as seguintes:
- Realizar a extração das informações que conseguir da base de dados da [SteamDB](https://steamdb.info/sales/)
- Armazenar os Dados no Google Big Query
- Exportar ou conectar os dados com o Google Sheets
- Enviar o link do Google Sheets
## Ideias inciais
Para resolver esse problema eu pensei inicialmente em criar a arquitetura abaixo:
![Captura de tela de 2023-07-03 13-33-46](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/bb7fcc96-6eab-46f1-aa5e-60d57429493c)

###### *Essa arquitetura foi construida com o auxilio do [Excalidraw](https://excalidraw.com/#json=LHona4siCKr7fdWN9eZ0R,YQ31RtQY-k46EifE-siSDw).*

O objetivo era construir um código em python, e implementa-lo no Google Cloud Function, que realizasse a raspagem da pagina e salvasse essas informações no Google Cloud Storage, então estando o Google Cloud Storage na Mesma Região de uma base de dados no Big Query, transferir os arquivos e por ultimo conectar esse dados ao Google Sheets.

## Dificuldades encontradas
Para realizar o Crawler incialmente tenti usar a biblioteca do **pandas**, mas retornava "**ERRO 403**", que é um erro de permissão negada.
Então eu tentei ultilizar outra biblioteca python, **requests**, porém retornava o mesmo erro. Ai o proximo passo foi passar no argumento *headers* da requisição com o **requests** o *User-Agent*, porém sem sucesso.
Diante disso imaginei que fosse o modo como essa bibliotecas funcionam, dai pensei em utilizar outra biblioteca python, o **selenium**, que costuma ser mais robusta pois simula os cliques na pagina, porém, apesar das diversas tentativas sempre tive como retorno o mesmo erro **ERRO 403**.
Me coloquei a pesquisar mais a respeito do problema e decobrir que o site do StemaDb não permite Crawler ou Scrapoing na pagina.

![Captura de tela de 2023-07-03 11-13-00](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/36e4e675-c389-42a8-8eeb-b215f9ce43f8)

Dessa forma não vi mais a possiblidade de ultilizar uma Google Cloud Function na resolução desse desafio como tinha pensado inicialmente.
Não satisfeito busquei outra solução, utilizar a biblioteca python **tabula** que consegue ler tabelas de um arquivo em pdf. A ideia era fazer o download manual de alguns arquivos e então ultilizando o **tabula** obter as informações e tratar, dai podia ultilzar uma Google Cloud Function para tratar arquivos. Porém, as tabelas do site do SteamDb tem sub informações como na imagem abaixo:

![Captura de tela de 2023-07-03 14-21-26](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/e5e4e17a-960b-45f0-8ada-189b50e6ab3f)

E deivido ao tempo do desafio que era de 72 horas e a complexidade para tratar corretamente essa subiinformações não seiria possivel realizar dessa forma.
Porém no texto do desafio diz realizar aa extração das informações que conseguir assim, resolvi de outra maneira o desafio.

## Como eu resolvi



