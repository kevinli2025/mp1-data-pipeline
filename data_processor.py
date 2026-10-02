import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    prev_len = len(df)
    new_df = df.drop_duplicates()
    after_len = len(new_df)
    logger.debug(f"number of rows removed: {prev_len - after_len}")
    return new_df


def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    new_df = df.dropna(axis=0)
    return new_df


def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    pass


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    pass


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    pass