## Clone the repository

```bash
git clone https://github.com/jpnotsodev/shopflow.git
cd ~/shopflow
```

## Setup the virtual environment

To create a virtual environment:
```bash
python3 -m venv .venv
```

Activate the virtual environment:
```bash
source .venv/bin/activate
```

## Install the required packages

Inside the virtual environment, run the following command:
```bash
(.venv)/home/administrator/shopflow$ /bin/bash install_requirements.sh
```

Activate the virtual environment:
```bash
source .venv/bin/activate
```

## Verify the installed packages

```bash
python3 -c "import pyspark, duckdb; print(f\"pyspark ver: {pyspark.__version__}\n,duckdb ver: {duckdb.__version__}\")"
```

Output should look like this:

```bash
pyspark ver: 4.2.1
duckdb ver: 1.5.6
```

## Mock data set

You must first create fake data sets which you could later use for the data ingestion process. 

* `customers.csv` - contains a list of customers.
* `products.json` - contains a list of products.

To generate mock data, run:

```bash
python3 make_sources.py
```

## Data set quality

```bash
cut -d , -f 4 sources/customer.csv | sort | uniq -c
```

Output:

```bash
    271  lahore 
    312 Austin
    265 Dubai
    318 Karachi
    271 LONDON
    297 Lahore
    276 Toronto
      1 city
```

```bash
python3 -c "import os; print([(file, os.stat(os.path.join('data/raw/orders', dir, file)).st_size) for dir in os.listdir('data/raw/orders/') for file in os.listdir(f'data/raw/orders/{dir}')])"
```