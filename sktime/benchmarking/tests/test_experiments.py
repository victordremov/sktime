# -*- coding: utf-8 -*-
"""Functions to test the functions in experiments.py."""

import os.path

from sktime.benchmarking.experiments import (
    load_and_run_clustering_experiment,
    run_clustering_experiment,
)
from sktime.clustering import TimeSeriesKMeans
from sktime.utils.data_io import load_from_tsfile_to_dataframe as load_ts


def test_load_and_run_clustering_experiment():
    """Test loading, running and saving.

    Currently it just checks that the files have been created, then deletes them.
    Later it can be enhanced to check the results can be loaded.
    """
    load_and_run_clustering_experiment(
        overwrite=True,
        problem_path="../../datasets/data/",
        results_path="../Temp/",
        cls_name="kmeans",
        dataset="UnitTest",
        resample_id=0,
        train_file=True,
    )
    assert os.path.isfile("../Temp/kmeans/Predictions/UnitTest/testResample0.csv")
    assert os.path.isfile("../Temp/kmeans/Predictions/UnitTest/trainResample0.csv")
    os.remove("../Temp/kmeans/Predictions/UnitTest/testResample0.csv")
    os.remove("../Temp/kmeans/Predictions/UnitTest/trainResample0.csv")


def test_run_clustering_experiment():
    """Test running and saving results.

    Currently it just checks the files have been created, then deletes them.
    """
    data_dir = "../../datasets/data/"
    dataset = "UnitTest"
    train_X, train_Y = load_ts(data_dir + dataset + "/" + dataset + "_TRAIN.ts")
    test_X, test_Y = load_ts(data_dir + dataset + "/" + dataset + "_TEST.ts")
    run_clustering_experiment(
        train_X,
        TimeSeriesKMeans(n_clusters=2),
        results_path="../Temp/",
        trainY=train_Y,
        testX=test_X,
        testY=test_Y,
        cls_name="kmeans2",
        dataset_name=dataset,
        resample_id=0,
    )
    assert os.path.isfile("../Temp/kmeans2/Predictions/UnitTest/testResample0.csv")
    assert os.path.isfile("../Temp/kmeans2/Predictions/UnitTest/trainResample0.csv")
    os.remove("../Temp/kmeans2/Predictions/UnitTest/testResample0.csv")
    os.remove("../Temp/kmeans2/Predictions/UnitTest/trainResample0.csv")


test_run_clustering_experiment()