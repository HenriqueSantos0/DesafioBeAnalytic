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

Escrevi manualmente um arquivo em formato csv com algumas informações que consegui tirar da pagina e chamei de [testedados1.csv](https://github.com/HenriqueSantos0/DesafioBeAnalytic/blob/main/testedados1.csv).

Depois com o codigo [conveter.py](https://github.com/HenriqueSantos0/DesafioBeAnalytic/blob/main/converter.py) converti as informações de csv para parquet por se tratar de um formato de arquivo mais robusto e que ocupa menos espaço, obtendo assim o arquivo [tetedados1](https://github.com/HenriqueSantos0/DesafioBeAnalytic/blob/main/testedados1)

Depois disso fui no console da GCP e criei um projheto com o Nome de *DesafioBeAnalytics*

![Captura de tela de 2023-07-03 11-06-43](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/f861d5d4-fbbd-4db7-a929-4b552dd372e9)
![Captura de tela de 2023-07-03 11-06-56](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/1ed6e6d6-9b74-4315-b0bd-205260b0b4ba)

Então criei um Bucket no Google Cloud Storage para armazenar meu arquivo, seguindo a arquitetura já mensionada no inicio.

![Captura de tela de 2023-07-03 11-07-14](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/0fab4bda-d6e3-433d-9600-9ea112307bf9)

![Captura de tela de 2023-07-03 11-07-21](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/a80f71c8-7080-4983-a842-bb6f43bc32d6)

Dei ao Bucket o nome de Steam_db

![Captura de tela de 2023-07-03 11-08-06](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/5a6c85d7-333c-4105-8f24-826daa44c13c)

É importante nesse momento observar a região em que o Bucket será criado, pois o Big query só vai conseguir ler arquivos da mesma região.

![Captura de tela de 2023-07-03 11-08-15](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/c035e27c-484b-4e8a-be8b-10cb5e0d26c4)

Com o Bucket Criado

![Captura de tela de 2023-07-03 11-08-30](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/0471195a-f4b9-4a9b-a8ad-4f4a178cd71d)

Fiz o upload do arquivo

![Captura de tela de 2023-07-03 11-08-44](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/9894efae-573c-43ec-a6a4-9f6defaf8351)

Então fui para o serviço do Big Query

![Captura de tela de 2023-07-03 11-09-02](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/a256d10a-c015-43bf-a065-e397004dd1c7)

![Captura de tela de 2023-07-03 11-09-08](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/624424c4-364e-4ef8-a966-366034786905)

Cliquei em adicionar

![Captura de tela de 2023-07-03 11-09-14](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/e4256fb5-ff65-4ab5-b176-d02ce6de3795)

E busquei informações do Google Cloud Storage

![Captura de tela de 2023-07-03 11-09-20](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/31420dc8-a2ce-48b0-8f55-85e501acf2f1)

Preenchi com as informações nescessarias

![Captura de tela de 2023-07-03 11-09-55](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/3b472c85-392c-475a-adf6-54369ee027c3)

E então foi criado o conjunto de daods e a tabela

![Captura de tela de 2023-07-03 11-13-26](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/fcf23f9f-8214-48a9-a414-727951c2efb0)

**IMPORTANTE: O conjunto de dados deve estar na mesma região que o bucket para que op Big query possa transferir os dados.**

Derpois criei uma planilha no Google Sheets e fui em *Dados >> conector de dados >> Conectar ao Bigquery*

![Captura de tela de 2023-07-03 11-10-38](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/8310ccc1-b7bf-4063-9de2-fc3ec68d5690)

Dai então eu escolho o *projeto >> Conunto de dados >> tabela*

![Captura de tela de 2023-07-03 11-10-52](https://github.com/HenriqueSantos0/DesafioBeAnalytic/assets/89212899/5ccbe4b1-1f74-4215-ae30-4740294cd6bd)

**IMPORTANTE: A conta da GCP ultilizada é do mesmo e-mail onde criei o Google Shets**

Dessa forma conseguir consluir o desfaio e ter o link do [Google Sheets](https://docs.google.com/spreadsheets/d/13ytaG80gcRyqe7MIRlNgr8GRj7XUGqaqqjaUx8HKEmE/edit?usp=sharing) com as informações pedidas.




