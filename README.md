#  Apache Airflow: Financeiro

**Ideia do Projeto**

Consultar a bolsa de valores usando a API yFinance do Python.

*Fonte: Alura*

### Ambiente

Linux Ubuntu/
Airflow 2.3.2

### Bibliotecas

```bash
$ pip install yfinance
```

### Instalação 

```bash
$ cd ~/Documents
$ mkdir -p Financeirto/airflow
$ pip install 'apache-airflow[postgres, celery, redis]==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"
$ export AIRFLOW_HOME=/home/alura/Documents/Financeiro/airflow
$ airflow standalone
```

### Fase 1

```bash
$ cd /test
$ python3 yfinanceTest.py
$ mkdir csv
$ python3 yfinanceTest2.py
```

### Fase 2

Nesta fase as tarefas são executadas sequencialmente: 

* busca os registro do ticker AAPL, 
* depois GOOG, 
* depois MSFL 
* depois TSLA

A cada execusão os registros são salvos no formato .csv em /test/stocks

Airflow, executando a dag:

* get_stocks.py

### Fase 3

Configurando o LocalExecutor

```bash
$ sudo apt install postgresql postgresql-contrib
$ sudo -i -u postgres
$ createdb airflow_db
$ psql airflow_db
> CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
> GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
```

Configurando o **airflow.cfg**

```
# linha 24
executor = LocalExecutor

# linha 186
sql_alchemy_conn = postgresql+psycopg2://airflow_user:airflow_pass@localhost/airflow_db
```

Subindo o **Apache Airflow**

```bash
$ airflow db init
$ airflow standalone
```

Execute novamente o get_stocks.py. Perceba que agora todas as stocks foram processados em paralelo.

