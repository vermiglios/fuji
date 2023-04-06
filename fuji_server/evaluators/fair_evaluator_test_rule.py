# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2020 PANGAEA (https://www.pangaea.de/)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from fuji_server.evaluators.fair_evaluator import FAIREvaluator
from fuji_server.models.test_rule import TestRule
from fuji_server.models.test_rule_output import TestRuleOutput
from fuji_server.models.test_rule_output_inner import TestRuleOutputInner
import mimetypes
import re


class FAIREvaluatorTestRule(FAIREvaluator):
    """
    A class to evaluate whether the data is available in a file format recommended by the targe research community (R1.3-02D).
    A child class of FAIREvaluator.
    ...

    Methods
    -------
    evaluate()
        This method will evaluate whether the data format is available in a long-term format (as defined in ISO/TR 22299)
        or in open format (see e.g., https://en.wikipedia.org/wiki/List_of_open_formats) or in a scientific file format.
    """

    def evaluate(self):

        self.result = TestRule(id=self.metric_number,
                                     metric_identifier=self.metric_identifier,
                                     metric_name=self.metric_name)

        self.output = TestRuleOutput()
        data_file_list = []

        data_file_output = TestRuleOutputInner()
        data_file_output.prova = 'prova'

        data_file_list.append(data_file_output)

        self.setEvaluationCriteriumScore('FsF-F5-01D-1', 1, 'pass')
        self.setEvaluationCriteriumScore('FsF-F5-01D-2', 0, 'pass')
        self.maturity = 2
        self.score.earned = 1
        self.result.test_status = 'pass'

        self.output = data_file_list
        self.result.output = self.output
        self.result.metric_tests = self.metric_tests
        self.result.maturity = self.maturity
        self.result.score = self.score
