"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S"
    )  


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="check if file is valid")

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="what input file?"
    )

    parser.add_argument(
        "--output", "-o",
        required=True,
        help="output report filename"
    )

    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="output file format"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="show detailed DEBUG message"
    )

    args = parser.parse_args()

    return args


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    p = Path(filepath)
    if not p.is_file():
        logger.error(f"File not found: '{filepath}'")
    
    



def main():
    """Main pipeline function."""
    pass  # TODO: implement


if __name__ == "__main__":
    main()