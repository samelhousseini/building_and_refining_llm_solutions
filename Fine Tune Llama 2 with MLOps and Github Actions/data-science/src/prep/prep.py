# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Prepares raw data and provides training, validation and test datasets
"""

import argparse

from pathlib import Path
import os
import numpy as np
import pandas as pd
import json

import mlflow


def parse_args():
    '''Parse input arguments'''

    parser = argparse.ArgumentParser("prep")
    parser.add_argument("--raw_data", type=str, help="Path to raw data")
    parser.add_argument("--train_data", type=str, help="Path to train dataset")
    parser.add_argument("--val_data", type=str, help="Path to test dataset")
    parser.add_argument("--test_data", type=str, help="Path to test dataset")
   
   
    args = parser.parse_args()

    return args


def main(args):
    '''Read, split, and save datasets'''

    # ------------ Reading Data ------------ #
    # -------------------------------------- #

    print("mounted_path files: ")


    with open(Path(args.raw_data)) as f:
        data = pd.DataFrame(json.loads(line) for line in f)


    # ------------- Split Data ------------- #
    # -------------------------------------- #

    # Split data into train, val and test datasets

    random_data = np.random.rand(len(data))

    msk_train = random_data < 0.7
    msk_val = (random_data >= 0.7) & (random_data < 0.85)
    msk_test = random_data >= 0.85

    train = data[msk_train]
    val = data[msk_val]
    test = data[msk_test]

    mlflow.log_metric('train size', train.shape[0])
    mlflow.log_metric('val size', val.shape[0])
    mlflow.log_metric('test size', test.shape[0])

    # train.to_parquet((Path(args.train_data) / "train.parquet"))
    # val.to_parquet((Path(args.val_data) / "val.parquet"))
    # test.to_parquet((Path(args.test_data) / "test.parquet"))

    # train.to_json((Path(args.train_data) / "train.jsonl"), orient='records', lines=True)
    # val.to_json((Path(args.val_data) / "val.jsonl"), orient='records', lines=True)
    # test.to_json((Path(args.test_data) / "test.jsonl"), orient='records', lines=True)

    train.to_json((Path(args.train_data) ), orient='records', lines=True)
    val.to_json((Path(args.val_data) ), orient='records', lines=True)
    test.to_json((Path(args.test_data)), orient='records', lines=True)


if __name__ == "__main__":

    mlflow.start_run()

    # ---------- Parse Arguments ----------- #
    # -------------------------------------- #

    args = parse_args()

    lines = [
        f"Raw data path: {args.raw_data}",
        f"Train dataset output path: {args.train_data}",
        f"Val dataset output path: {args.val_data}",
        f"Test dataset path: {args.test_data}",

    ]

    for line in lines:
        print(line)
    
    main(args)

    mlflow.end_run()

    