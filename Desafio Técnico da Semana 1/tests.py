# import os
from unittest import TestCase, mock

import settings
from stock_time_series import StockTimeSeries
from stock_time_series.stock_series import requests
from core.exceptions import APICallError


class MockedResponse:

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs

    @property
    def status_code(self):
        return self.kwargs.get("status_code") or 200

    def json(self, *args, **kwargs):
        return self.kwargs.get("json_return_value") or {}


class TestStockTimeSeries(TestCase):

    def setUp(self):
        settings.APIKEY = "sampleapikey"
        settings.BASE_URL = "http://example.com/query"

        self.stock_time_series_obj = StockTimeSeries()


    def test_obj_created_with_expected_attributes(self):
        attrs = [
            ("api_key", "sampleapikey"),
            ("base_url", "http://example.com/query")
        ]

        for attr, value in attrs:
            with self.subTest():
                self.assertEqual(
                    getattr(self.stock_time_series_obj, attr), value
                )

    def test_build_url(self):
        expected = "http://example.com/query?foo=bar&apikey=sampleapikey"
        actual = self.stock_time_series_obj._build_url("foo=bar")

        self.assertEqual(expected, actual)

    @mock.patch.object(requests, "get")
    def test_intraday_series(self, mock_get):
        mock_get.return_value = MockedResponse()
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": "IBM",
            "interval": "5m"
        }

        self.stock_time_series_obj.intraday_series(**params)
        mock_get.assert_called_with(
            "http://example.com/query?"
            "function=TIME_SERIES_INTRADAY&"
            "symbol=IBM&"
            "interval=5m&"
            "apikey=sampleapikey"
        )

    @mock.patch.object(requests, "get")
    def test_intraday_series_raises_api_call_error(self, mock_get):
        mock_get.return_value = MockedResponse(status_code="NOT_OK")
        expected_error_message = (
            "Não foi possivel consumir o serviço: STATUS_CODE=NOT_OK"
        )
        with self.assertRaisesRegex(APICallError, expected_error_message):
            params = {
                "function": "TIME_SERIES_INTRADAY",
                "symbol": "IBM",
                "interval": "5m"
            }

            self.stock_time_series_obj.intraday_series(**params)
