import os
import sys

import tabula
from tabula import read_pdf

def extract_tables_to_tsv(pdf_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read tables from PDF
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    out_fn_prefix = os.path.basename(pdf_path).split('.')[0]

    # Loop through the found tables
    for index, table in enumerate(tables):
        output_path = os.path.join(output_folder, f"{out_fn_prefix}_{index+1}.tsv")
        # Save each table as a TSV file
        table.to_csv(output_path, sep='\t', index=False)
        print(f"Saved: {output_path}")

in_pdf = sys.argv[1]
out_folder = sys.argv[2]

# Replace 'path_to_pdf.pdf' with the path to your PDF file
# Replace 'output_folder' with the desired path to save the TSV files
extract_tables_to_tsv( in_pdf, out_folder )
