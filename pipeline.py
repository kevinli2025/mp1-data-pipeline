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
    pass  # TODO: implement


def parse_arguments():
    parser = argparse.ArgumentParser(description="check if file is valid")

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="what input file?"
    )

    parser.add_argument(
        "--output", "-o",
        required=True,
        help="what output file?"
    )

    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true"
    )

    args = parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    pass  # TODO: implement


def main():
    """Main pipeline function."""
    pass  # TODO: implement


if __name__ == "__main__":
    main()