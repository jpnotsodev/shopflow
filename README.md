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