import argparse
import logging
import sys
from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)

logger = logging.getLogger(__name__)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="check if file is valid")

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="process input data file"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="path to YAML config file"
    )

    parser.add_argument(
        "--output", "-o",
        required=True,
        help="output report filename"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="show detailed DEBUG message"
    )

    args = parser.parse_args()

    return args
    
def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(f"Arguments parsed: input={args.input}, output={args.output}, config={args.config}")
    if not validate_input(args.input):
        sys.exit(1)

    if not validate_input(args.config):
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)

    except ValueError:
        sys.exit(1)

    prev_data = data.copy()

    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]

    prev_len = len(data)
    
    try:
        data = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)

    logger.info(f"Validation complete: {prev_len} -> {len(data)} rows")

    try:
        data = process_data(data, config)
    except ValueError:
        sys.exit(1)

    logger.info(f"Processing complete: {len(prev_data)} -> {len(data)} rows")

    save_data(data, args.output)

    logger.info(f"Saved cleaned data to {args.output}")

    report = create_cleaning_report(prev_data, data)
    print("Cleaning report:")
    print(report)
    

if __name__ == "__main__":
    main()