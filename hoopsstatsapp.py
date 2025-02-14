"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(frame):
    """
    Cleans the basketball statistics data frame by splitting columns
    that contain makes-attempts values into separate columns.
    """
    for col in ["FG", "3PT", "FT"]:
        if col in frame.columns:
            new_cols = frame[col].str.split('-', expand=True).astype(float)
            frame[f"{col}M"] = new_cols[0]
            frame[f"{col}A"] = new_cols[1]
            frame.drop(columns=[col], inplace=True)
    
    return frame

def main():
    """Creates the data frame and view and starts the app."""
    file_name = "rawbrogdonstats.csv"
    frame = pd.read_csv(file_name)
    
    print("Before Cleaning:")
    print(frame.head())

    frame = cleanStats(frame)

    print("\nAfter Cleaning:")
    print(frame.head())

    HoopStatsView(frame)

if __name__ == "__main__":
    main()
