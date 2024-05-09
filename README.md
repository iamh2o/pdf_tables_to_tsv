# Overview
* Given a pdf, extract all tables w/in the pdf as independent TSV files.
* This tools often works, but should not be considered stable/prod ready.
* Tested on mac 14.1.1
* good luck!

# Conda env

```bash

conda create -n PT2T -c conda-forge python pip ipython parallel

```

# Pip install other libs

```bash
conda activate PT2T
pip install tabula tabula-py
```

# Run the Tool

```bash
conda activate PT2T

python bin/pdf_table_x.py ./some_document.pdf ./out/

```

* This will attempt to extract any detected table as a file named {file_basename}_{ctr}.tsv
* A fair number of pdfs fail to parse on MAC 14.1.1 for various java and font problems not yet looked into.