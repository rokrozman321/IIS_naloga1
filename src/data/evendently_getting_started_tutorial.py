#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing

from evidently import ColumnMapping

from evidently.report import Report
from evidently.metrics.base_metric import generate_column_metrics
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, DataQualityPreset, RegressionPreset
from evidently.metrics import *

from evidently.test_suite import TestSuite
from evidently.tests.base_test import generate_column_tests
from evidently.test_preset import DataStabilityTestPreset, NoTargetPerformanceTestPreset, RegressionTestPreset
from evidently.tests import *


# In[2]:


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')


# In[3]:


# load data

file1 = "data/processed/reference_data.csv" 
file2 = "data/processed/current_data.csv" 

reference = pd.read_csv(file1)
current = pd.read_csv(file2)


# In[4]:


# reference


# In[5]:


# current


# In[6]:


report = Report(metrics=[
    DataDriftPreset(), 
])

report.run(reference_data=reference, current_data=current)
# report


# In[7]:


report.as_dict()
report.json()
report.save_html('reports/report.html')
report.save_json('reports/report.json')


# In[8]:


tests = TestSuite(tests=[
    TestNumberOfColumnsWithMissingValues(),
    TestNumberOfRowsWithMissingValues(),
    TestNumberOfConstantColumns(),
    TestNumberOfDuplicatedRows(),
    TestNumberOfDuplicatedColumns(),
    TestColumnsType(),
    TestNumberOfDriftedColumns(),
])

tests.run(reference_data=reference, current_data=current)
# tests


# In[ ]:


tests.as_dict()
tests.json()
tests.save_html('reports/tests.html')
tests.save_json('reports/tests.json')

