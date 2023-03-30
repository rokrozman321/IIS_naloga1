from pprint import pprint
import numpy as np
from sklearn.linear_model import LinearRegression
import mlflow
from mlflow import MlflowClient
import os


def fetch_logged_data(run_id):
    client = MlflowClient()
    data = client.get_run(run_id).data
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    return data.params, data.metrics, tags, artifacts

MLFLOW_TRACKING_URI="https://dagshub.com/rokrozman321/IIS_naloga1.mlflow"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# enable autologging
mlflow.sklearn.autolog()

# prepare training data
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# train a model
model = LinearRegression()
with mlflow.start_run() as run:
    model.fit(X, y)

# fetch logged data
params, metrics, tags, artifacts = fetch_logged_data(run.info.run_id)

pprint(params)
# {'copy_X': 'True',
#  'fit_intercept': 'True',
#  'n_jobs': 'None',
#  'normalize': 'False'}

pprint(metrics)
# {'training_score': 1.0,
#  'training_mean_absolute_error': 2.220446049250313e-16,
#  'training_mean_squared_error': 1.9721522630525295e-31,
#  'training_r2_score': 1.0,
#  'training_root_mean_squared_error': 4.440892098500626e-16}

pprint(tags)
# {'estimator_class': 'sklearn.linear_model._base.LinearRegression',
#  'estimator_name': 'LinearRegression'}

pprint(artifacts)
# ['model/MLmodel', 'model/conda.yaml', 'model/model.pkl']