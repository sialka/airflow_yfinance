#  Apache Airflow: Financeiro

**Ideia do Projeto**

Consultar a bolsa de valores usando a API yFinance do Python.

*Fonte: Alura*

### Ambiente

Linux Ubuntu
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
