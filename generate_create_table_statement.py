import csv

# change folder as needed
tsv_file = 'C:\\Users\\username\\folder\\tara_data.tsv'
out_file = 'C:\\Users\\username\\folder\\create_table_statement.txt'

with open(tsv_file, newline='') as f, open(out_file, 'w') as outfile:
    reader = csv.reader(f, delimiter='\t')
    for i, row in enumerate(reader):
        if i == 0:  # Only generate table statement for header row
            table_name = 'tara_dataset'  # Replace with your desired table name
            columns = [f'{col.replace(",", "_")} integer default 0' for col in row]
            table_statement = f'CREATE TABLE {table_name} ({", ".join(columns)});'
            outfile.write(table_statement)
            outfile.write('\n')
            break
