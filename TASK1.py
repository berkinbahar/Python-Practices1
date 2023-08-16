# Import libraries
import pandas as pd
import numpy as np

worker = pd.read_csv("path_worker")
worker.head()

title = pd.read_csv("path_title")
title.head()

title_new = title.rename(columns={"worker_ref_id" : "worker_id"})
merged_df = pd.merge(worker, title_new, on="worker_id")
max_salary = merged_df[merged_df["salary"] == merged_df["salary"].max()][["worker_title"]]
result = max_salary.rename(columns={"worker_title": "best_paid_title"})

type(result)
