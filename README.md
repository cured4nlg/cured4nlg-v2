# CURED4NLG (v2) Dataset

This repository contains the data and scripts for the CURED4NLG (v2) dataset. 

## Set up environment and libraries.

Create and activate a virtual environment using Anaconda.
```sh
conda create -n cured4nlg-v2 python=3.11
conda activate cured4nlg-v2
```

Install the required libraries.
```sh
pip install -r requirements.txt
```

## Extract tables and texts from pdf (as `.md`).

```sh
mkdir -p ./ocr/v2/markdown
mkdir -p ./ocr/v2/table_markdown

marker ./pdf/v2 --workers 1 --max_tasks_per_worker 1 --output_format markdown --output_dir ./ocr/v2/markdown
marker ./pdf/v2 --workers 1 --max_tasks_per_worker 1 --output_format markdown --output_dir ./ocr/v2/table_markdown --converter_cls marker.converters.table.TableConverter
```

## Procedure for creating the dataset

The following steps were taken to create the final dataset

1. Tables
	1. Convert tables in markdown to TSV/CSV format (see `scripts/md2tsv.py`).
	1. Find and replace extraneous characters (e.g., markup symbols, footnotes, etc.) (see `scripts/fix-symbols.sh`).
	1. Fix cells which span multiple rows in a table (see `scripts/fix-multi-row`).
2. Texts
	1. Extract relevant text from markdown and remove extraneous characters (e.g., markup symbols, footnotes, etc.).
	1. Remove references to figures and tables in the texts (see `scripts/remove-fig-tab-ref.sh`).
	1. Normalize numbers in texts (e.g., 1 234 567 is converted to 1234567) (see `scripts/normalize-numbers.sh`).
	1. Remove sentences from each text that cannot be verified from its corresponding table.
	1. Remove other extraneous sentences that are unrelated to the input table, e.g., cautionary statements, warnings, disclaimers, footnotes etc.
	1. Fix typos, inconsistent spellings, leading/trailing spaces, etc.
