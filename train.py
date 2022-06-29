import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts, set_tracking_uri, set_experiment

set_tracking_uri("http://ec2-44-204-62-53.compute-1.amazonaws.com:5000/")
set_experiment("scikit-learn")


if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("param1", randint(0, 100))

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)

    # Log an artifact (output file)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world Mario!")
    log_artifacts("outputs")