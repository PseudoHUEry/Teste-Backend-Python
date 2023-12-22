# Desafio

Desenvolver um web scraper em Python para extrair dados de população de países da página "Scrape This Site" e estruturar esses dados em formato JSON. Além disso, enviar os dados estruturados para uma fila no Kafka.

# Deploy

É possível executar o projeto em duas frentes. Cada entidade individualmente, ou, caso haja o Docker Compose em sua máquina, é possível utilizar o comando a seguir:

```bash
docker-compose up --build
```

# Resultado

FrontEnd
    Interface para chamada de endpoint para consumo e exibição de dados.
- [FrontEnd](http://localhost)

BackEnd
    FastAPI para chamada do endpoint que possui a responsabilidade de executar a varredura de dados na página "Scrape This Site", tratar dados, envia-los em um tópico estabelecido nas variáveis de ambiente, armazenar todas informações no banco MongoDb e retornar todos os parâmetros retirados da Pagina.
    Incluso Swaggear, podendo o mesmo ser encontrado em: 
- [Swaggear](http://0.0.0.0:8000/docs)
     
Banco De Dados - MongoDB
    Implementação de banco NoSQL para armazenar dados.
- URI: mongodb://localhost:27017/

Kafka
    Implementação de Kafka e Zookeper para gestão e criação de Tópicos. Adicionado Kafdrop para que seja possivel a visualização das filas através interface.
- [Kafdrop](http://localhost:19000)
 