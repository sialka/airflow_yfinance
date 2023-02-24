#  Apache Airflow: Financeiro

**Ideia do Projeto**

Consultar a bolsa de valores usando a API yFinance do Python.
No Airflow começamos com execuções de tarefas sequenciais, depois em paralelas.

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

Nesta fase usamos o executor **SequentialExecutor**, onde as tarefas são executadas sequencialmente: 

* busca os registro do ticker AAPL, 
* depois GOOG, 
* depois MSFL 
* depois TSLA

A cada execusão os registros são salvos no formato .csv em /test/stocks

Airflow, executando a dag:

* get_stocks.py

### Fase 3

Nesta fase usamos o executor **LocalExecutor**, as tarefas são executados em paralelo, limitando-se aos recursos da máquina.

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

### Fase 4

Nesta fase usaremos o executor **CeleryExecutor**, as tarefas serão executadas em filas. 
As tarefas serão enviadas para os **Workers** (máquinas individuais) ou seja as tarefas serão dividas para várias máquinas,
se uma falhar as outras continuam trabalhando até que termine a fila de tarefas.

**Instalando o Redis:**

```bash
$ wget https://caelum-online-public.s3.amazonaws.com/2606-aprofundando-airflow-executor-celery/01/redis-7.0.4.tar.gz
$ tar -xf redis-7.0.4.tar.gz
$ cd redis-7.0.4/
$ make
$ sudo make install
$ redis-server
```

**Configurando:**

```python
# File: airflow.cfg (Linha 24)
executor = CeleryExecutor
# (linha 810/)
broker_url = redis://0.0.0.0:6379/0
# (linha 817)
result_backend = db+postgresql://airflow_user:airflow_pass@localhost/airflow_db
```

**Subindo as Instancias**


Usaremos 5 Terminais, observação em todos os terminais habilitar o ambiente virtual (venv) e a variável de ambiente AIRFLOW_HOME.

| Terminal 1 - Redis
```bash
# Na pasta do Redis-7.0.4
$ redis-server
```

| Terminal 2 - Airflow Scheduler
```bash
$ airflow scheduler
```

| Terminal 3 - Airflow Scheduler
```bash
$ airflow webserver
```

Neste ponto, execute no navegador: localhost:8080 observe que as tarefas estão em filas mas não foram executadas.

| Terminal 4 - Airflow Celery Flower
```bash
$ airflow celery flower
```

Neste ponto, execute no navegado em outra aba: localhost:5555 observe que ainda não temos um Broker para executar as tarefas

| Terminal 5 - Airflow Scheduler
```bash
$ airflow celery worker
```

Agora sim as tarefas serão executadas