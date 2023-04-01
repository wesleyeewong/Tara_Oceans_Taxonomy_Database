import csv
import fileinput
import shutil
import tempfile


# Change as needed
tsv_file = 'C:\\Users\\username\\folder\\tara_data.tsv'
tsv_out = 'C:\\Users\\username\\folder\\tara_data_out_2.tsv'
modified_header = ''

# Get and modify header
with open(tsv_file, 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    header = next(reader)
    modified_header = [col.replace(',', '_') for col in header]

with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    with open(tsv_file, 'r', newline='') as f:
        writer = csv.writer(temp_file, delimiter='\t', lineterminator='')
        writer.writerow(modified_header)
        temp_file.write('\n')
        # Skip the first row (header)
        header = next(f)
        print(repr(header[-5:]))
        first = next(f)
        # Copy the remaining rows to the temporary file
        shutil.copyfileobj(f, temp_file)

# Move temp file to tsv_out location
shutil.move(temp_file.name, tsv_out)
