# Tara_Oceans_Taxonomy_Database

## Pre-requisites

* python3 installed
* postgreSQL (version 15) database installed
* basic command line knowledge


## Re-format header
Headers on the Tara Oceans TSV dataset has commas in them, we just want to change them to underscores

Open the `format_header.py` file, and modify the folder variables as needed, note that current folder structure is specifically for Windows:
```
tsv_file = 'C:\\Users\\username\\folder\\tara_data.tsv'
tsv_out = 'C:\\Users\\username\\folder\\tara_data_out_2.tsv'
```

Save and open up your command line, `cd` to the folder where the scripts are located, then run the script:
`python format_header.py`

## Generate create table statement
Since there're over 900 columns it's easier to generate the create table statement via script as well.

The script is currently setting all column data types to be `integer` and defaults to 0. After you generate the statement some of the columns' (7) data type will need to be changed to `text`.

Open the `generate_create_table_statement.py` file, and modify the folder variables as needed, note that current folder structure is specifically for Windows:
```
tsv_file = 'C:\\Users\\username\\folder\\tara_data.tsv'
out_file = 'C:\\Users\\username\\folder\\create_table_statement.txt'
```

And the table name you want, line 11:
```
table_name = 'tara_dataset'  # Replace with your desired table name
```

Save, and in your command line run the script:
`python generate_create_table_statement.py`

Then open up the text file with the create table statement on it, these are the columns you need to change:
* At the very beginning:
	* cid
	* md5sum
	* sequence
* At the very end:
	* pid
	* refs
	* lineage
	* taxogroup

Example:
Change
```
CREATE TABLE table_name (cid integer default 0, md5sum integer default 0 ...
```
to
```
CREATE TABLE table_name (cid text default 'null', md5sum text default 'null ...
```

If you know what you're doing, feel free to change it to whatever data type you see fit, this is just for simplicity.

After that you can simply copy the create statement and paste it into Postgres to create the table.

## Import data to PostgreSQL
For this part you'd need to do it in Postgres command line mode. I also highly recommend installing the pgAmin tool beforehand to create your database.

In the command line type in:
`psql -U postgres`

To login to postgres, replace `postgres` to whatever user you've created when setting up. It might also prompt your for your password.

After you've successfully logged in you should see something like so:
`postgres_or_whatever_your_username_is=#`

First connect to the database you want to create the table on:
`\c 'database name'`

Actual import command:
```
\copy your_table_name_here from 'C:\\Users\\username\\folder\\tara_dataset_header_formatted.tsv' DELIMITER E'\t' CSV HEADER;
```

Copy that into the Postgres command line then hit enter. If nothing happens immediately, that means it's running. If there are any errors it'll let you know, if it successfully copied everything you'll see something like this:
`COPY 123423`
