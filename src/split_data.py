import pandas as pd
from pathlib import Path

# Project root = one level up from this file (src/)
root = Path(__file__).resolve().parents[1]

data_raw_path = root / "data_raw"
data_working_path = root / "data_working"
test_path = root / "Data"

csv_name = "anxiety_depression_data.csv"

# Load full dataset
df = pd.read_csv(data_raw_path / csv_name)

# 20% test set
test_df = df.sample(frac=0.2, random_state=42)

# Remaining 80% 
train_df = df.drop(test_df.index)


data_working_path.mkdir(exist_ok=True)
test_path.mkdir(exist_ok=True)

# Save files
test_df.to_csv(test_path / "test.csv", index=False)
train_df.to_csv(data_working_path / "train.csv", index=False)

print("Created:")
print(f"  - Test set: {test_path / 'test.csv'} (20%)")
print(f"  - Train set: {data_working_path / 'train.csv'} (80%)")

