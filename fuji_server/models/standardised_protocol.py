# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server.models.debug import Debug  # noqa: F401,E501
from fuji_server.models.fair_result_common import FAIRResultCommon  # noqa: F401,E501
from fuji_server.models.fair_result_common_score import FAIRResultCommonScore  # noqa: F401,E501
from fuji_server.models.standardised_protocol_output import StandardisedProtocolOutput  # noqa: F401,E501
from fuji_server import util


class StandardisedProtocol(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, metric_identifier: str=None, metric_name: str=None, test_status: str='fail', score: FAIRResultCommonScore=None, output: StandardisedProtocolOutput=None, test_debug: Debug=None):  # noqa: E501
        """StandardisedProtocol - a model defined in Swagger

        :param id: The id of this StandardisedProtocol.  # noqa: E501
        :type id: int
        :param metric_identifier: The metric_identifier of this StandardisedProtocol.  # noqa: E501
        :type metric_identifier: str
        :param metric_name: The metric_name of this StandardisedProtocol.  # noqa: E501
        :type metric_name: str
        :param test_status: The test_status of this StandardisedProtocol.  # noqa: E501
        :type test_status: str
        :param score: The score of this StandardisedProtocol.  # noqa: E501
        :type score: FAIRResultCommonScore
        :param output: The output of this StandardisedProtocol.  # noqa: E501
        :type output: StandardisedProtocolOutput
        :param test_debug: The test_debug of this StandardisedProtocol.  # noqa: E501
        :type test_debug: Debug
        """
        self.swagger_types = {
            'id': int,
            'metric_identifier': str,
            'metric_name': str,
            'test_status': str,
            'score': FAIRResultCommonScore,
            'output': StandardisedProtocolOutput,
            'test_debug': Debug
        }

        self.attribute_map = {
            'id': 'id',
            'metric_identifier': 'metric_identifier',
            'metric_name': 'metric_name',
            'test_status': 'test_status',
            'score': 'score',
            'output': 'output',
            'test_debug': 'test_debug'
        }
        self._id = id
        self._metric_identifier = metric_identifier
        self._metric_name = metric_name
        self._test_status = test_status
        self._score = score
        self._output = output
        self._test_debug = test_debug

    @classmethod
    def from_dict(cls, dikt) -> 'StandardisedProtocol':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StandardisedProtocol of this StandardisedProtocol.  # noqa: E501
        :rtype: StandardisedProtocol
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this StandardisedProtocol.


        :return: The id of this StandardisedProtocol.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this StandardisedProtocol.


        :param id: The id of this StandardisedProtocol.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metric_identifier(self) -> str:
        """Gets the metric_identifier of this StandardisedProtocol.


        :return: The metric_identifier of this StandardisedProtocol.
        :rtype: str
        """
        return self._metric_identifier

    @metric_identifier.setter
    def metric_identifier(self, metric_identifier: str):
        """Sets the metric_identifier of this StandardisedProtocol.


        :param metric_identifier: The metric_identifier of this StandardisedProtocol.
        :type metric_identifier: str
        """
        if metric_identifier is None:
            raise ValueError("Invalid value for `metric_identifier`, must not be `None`")  # noqa: E501

        self._metric_identifier = metric_identifier

    @property
    def metric_name(self) -> str:
        """Gets the metric_name of this StandardisedProtocol.


        :return: The metric_name of this StandardisedProtocol.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
        """Sets the metric_name of this StandardisedProtocol.


        :param metric_name: The metric_name of this StandardisedProtocol.
        :type metric_name: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def test_status(self) -> str:
        """Gets the test_status of this StandardisedProtocol.


        :return: The test_status of this StandardisedProtocol.
        :rtype: str
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status: str):
        """Sets the test_status of this StandardisedProtocol.


        :param test_status: The test_status of this StandardisedProtocol.
        :type test_status: str
        """
        allowed_values = ["pass", "fail", "indeterminate"]  # noqa: E501
        if test_status not in allowed_values:
            raise ValueError(
                "Invalid value for `test_status` ({0}), must be one of {1}"
                .format(test_status, allowed_values)
            )

        self._test_status = test_status

    @property
    def score(self) -> FAIRResultCommonScore:
        """Gets the score of this StandardisedProtocol.


        :return: The score of this StandardisedProtocol.
        :rtype: FAIRResultCommonScore
        """
        return self._score

    @score.setter
    def score(self, score: FAIRResultCommonScore):
        """Sets the score of this StandardisedProtocol.


        :param score: The score of this StandardisedProtocol.
        :type score: FAIRResultCommonScore
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def output(self) -> StandardisedProtocolOutput:
        """Gets the output of this StandardisedProtocol.


        :return: The output of this StandardisedProtocol.
        :rtype: StandardisedProtocolOutput
        """
        return self._output

    @output.setter
    def output(self, output: StandardisedProtocolOutput):
        """Sets the output of this StandardisedProtocol.


        :param output: The output of this StandardisedProtocol.
        :type output: StandardisedProtocolOutput
        """

        self._output = output

    @property
    def test_debug(self) -> Debug:
        """Gets the test_debug of this StandardisedProtocol.


        :return: The test_debug of this StandardisedProtocol.
        :rtype: Debug
        """
        return self._test_debug

    @test_debug.setter
    def test_debug(self, test_debug: Debug):
        """Sets the test_debug of this StandardisedProtocol.


        :param test_debug: The test_debug of this StandardisedProtocol.
        :type test_debug: Debug
        """

        self._test_debug = test_debug
