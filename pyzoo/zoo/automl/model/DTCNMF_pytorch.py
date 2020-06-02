# Copyright 2018 Analytics Zoo Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from abc import ABC

from zoo.automl.common.metrics import Evaluator
import pandas as pd
from zoo.automl.model.abstract import BaseModel
from zoo.automl.common.util import save_config


class DTCNMFPytorch(BaseModel):
    """
    MF regularized TCN + TCN. This version is not for automated searching yet.
    """

    def __init__(self, check_optional_config=False, future_seq_len=1):
        """
        Initialize hyper parameters
        :param check_optional_config:
        :param future_seq_len:
        """
        # models
        self.model_init = False
        self.X = None  # latent x vectors from Matrix Factorization
        self.F = None  # latent f vectors from Matrix Factorization
        self.XseqM = None  # a TCN model for latent vectors X
        self.YseqM = None  # a TCN model for Y

    def set_params(self, **config):
        self.vbsize = config.get("vbsize", None),
        self.hbsize = config.get("hbsize", None),
        self.num_channels_X = config.get("num_channels_X", None)
        self.num_channels_Y = config.get("num_channels_Y", None)
        self.kernel_size = config.get("kernel_size", None)
        self.dropout = config.get("dropout", None)
        self.rank = config.get("rank", None)
        self.kernel_size_Y = config.get("kernel_size_Y", None)
        self.val_len = config.get("val_len", None)
        self.end_index = config.get("end_index", None)
        self.normalize = config.get("normalize", None)
        self.start_date = config.get("start_date", None)
        self.freq = config.get("freq", None)
        self.use_time = config.get("use_time", None)
        self.dti = config.get("dti", None)
        self.svd = config.get("svd", None)
        self.period = config.get("period", None)
        self.forward_cov = config.get("forward_cov", None)

    def build(self, mc=False, **config):
        """
        build the models and initialize.
        :param mc: mc dropout, Ignored.
        :param config: hyper parameters for building the model
        :return:
        """
        # TODO build model and initialize
        self.model_init = True

    def fit_eval(self, x, y=None, validation_data=None, mc=False, verbose=0, **config):
        """
        Fit on the training data from scratch.
        Since the rolling process is very customized in this model,
        we enclose the rolling process inside this method.

        :param x: training data, an array in shape (nd, Td),
            nd is the number of series, Td is the time dimension
        :param y: None. target is extracted from x directly
        :param validation_data: None. validation set is extracted from x directly
        :param mc: mc dropout
        :param verbose:
        :param config:
        :return: the evaluation metric value
        """
        if not self.model_init:
            self.build(mc=mc, **config)
        # TODO train_all_models
        pass

    def fit_incremental(self, x, **config):
        """
        Incremental fitting given a pre-trained model.
        :param x: incremental data
        :param config: fitting parameters
        :return:
        """
        # TODO incrementally train models
        pass

    def predict(self, x, mc=False, ):
        """

        :param x:
        :param mc:
        :return:
        """
        # TODO predict on new data
        pass

    def evaluate(self, x, y, metric=None):
        """
        Evaluate on x, y
        :param x: input
        :param y: target
        :param metric: a list of metrics in string format
        :return: a list of metric evaluation results
        """
        pass

    def save(self, model_path, config_path):
        raise NotImplementedError

    def restore(self, model_path, **config):
        raise NotImplementedError

    def _get_optional_parameters(self):
        return {}

    def _get_required_parameters(self):
        return {}
