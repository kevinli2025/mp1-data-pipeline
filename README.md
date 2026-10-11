Overall, this pipeline takes in a raw dataset, validates its structure/values to see if it matches the requirements stored in a YAML file within the project, cleans it by removing duplicates, missing values, and outliers, then returns a cleaned dataset and a summary report. Everything starts with the user input in the terminal, for example: 
"python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose"
The pipeline then parses the command line arguments, sets up logging, then checks if the input file is valid. Next, data_loaders.py loads the input and config files and data_validator.py checks if the input file satisfies the required columns and valid numeric values. The validated data is then passed to data_processor where duplicates, missing values, and outliers are removed all according to the config YAML settings. Then, data_output.py saves the cleaned dataset as a CSV file, pipeline generates a cleaning summary of the changes. Utils.py contains reusable functions for setting up and checking input files, and src/__init__.py puts the functions in one place and makes it importable to pipeline.py. 

example command: python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

code output:
16:33:24 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, output=output/clean.csv, config=config/config.yaml
16:33:24 INFO     src.utils — File validated: 'fixtures/sample_data.csv'
16:33:24 INFO     src.utils — File validated: 'config/config.yaml'
16:33:24 INFO     src.data_loaders — Loaded CSV file: sample_data.csv (100 rows)
16:33:24 INFO     src.data_loaders — Loaded YAML file: config.yaml
16:33:24 WARNING  src.data_validator — invalid numeric value at row 94
16:33:24 WARNING  src.data_validator — invalid numeric value at row 95
16:33:24 DEBUG    src.data_validator — validation: 100 -> 98 rows
16:33:24 INFO     __main__ — Validation complete: 100 -> 98 rows
16:33:24 DEBUG    src.data_processor — remove_duplicates: 98 -> 96 rows
16:33:24 DEBUG    src.data_processor — handle_missing: 96 -> 94
16:33:24 DEBUG    src.data_processor — rating: method = iqr, threshold = 1.5, rows removed = 2 
16:33:24 INFO     __main__ — Processing complete: 98 -> 92 rows
16:33:24 DEBUG    src.data_output — rows saved: 92 output path: output/clean.csv
16:33:24 INFO     __main__ — Saved cleaned data to output/clean.csv
Cleaning report:
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}