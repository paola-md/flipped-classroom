#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from extractor.feature.feature import Feature
from helper.dataset.data_preparation import get_sessions

class StdTimeSessions(Feature):

    def __init__(self, data, settings):
        super().__init__('std_time_sessions')
        self.data = data if 'week' not in settings else (data[data['week'] == settings['week']] if settings['timeframe'] == 'week' else data[data['week'] <= settings['week']])
        self.settings = settings

    def compute(self):
        if len(self.data.index) == 0:
            return 0.0
        return np.std(get_sessions(self.data.sort_values(by='date'), self.settings['max_session_length'], self.settings['min_actions'])['duration'])
