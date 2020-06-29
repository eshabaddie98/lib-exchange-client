# coding: utf-8

"""
    Blockchain.com Exchange REST API

    ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account Select API from the drop down menu Fill out form and click “Create New API Key Now” Once generated you can view your keys under API Settings   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.com.blockchain.exchange.rest.model.withdrawal_info import WithdrawalInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestWithdrawalInfo(unittest.TestCase):
    """WithdrawalInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WithdrawalInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.withdrawal_info.WithdrawalInfo()  # noqa: E501
        if include_optional :
            return WithdrawalInfo(
                withdrawal_id = '0', 
                amount = 12.23, 
                fee = 0.0005, 
                currency = 'BTC', 
                beneficiary = '0', 
                state = 'REJECTED', 
                timestamp = 1592830770594
            )
        else :
            return WithdrawalInfo(
                amount = 12.23,
                currency = 'BTC',
                beneficiary = '0',
        )

    def testWithdrawalInfo(self):
        """Test WithdrawalInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()