"""測試工具函數模組."""

import pytest
import requests
from unittest.mock import Mock, patch
from src.github_actions_practice.utils import (
    fetch_data,
    process_data,
    calculate_sum,
    is_even,
)


class TestFetchData:
    """測試 fetch_data 函數."""

    @patch("src.github_actions_practice.utils.requests.get")
    def test_fetch_data_success(self, mock_get):
        """測試成功取得資料."""
        # 模擬成功的回應
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_data("https://example.com")

        assert result == {"key": "value"}
        mock_get.assert_called_once_with("https://example.com", timeout=10)

    @patch("src.github_actions_practice.utils.requests.get")
    def test_fetch_data_http_error(self, mock_get):
        """測試 HTTP 錯誤."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        with pytest.raises(requests.HTTPError):
            fetch_data("https://example.com/notfound")


class TestProcessData:
    """測試 process_data 函數."""

    def test_process_data_simple_dict(self):
        """測試處理簡單字典."""
        data = {"a": 1, "b": 2, "c": 3}
        result = process_data(data)
        assert "找到 3 個鍵" in result
        assert "不包含巢狀結構" in result

    def test_process_data_nested_dict(self):
        """測試處理巢狀字典."""
        data = {"a": 1, "b": {"nested": True}, "c": [1, 2, 3]}
        result = process_data(data)
        assert "找到 3 個鍵" in result
        assert "包含巢狀結構" in result

    def test_process_data_empty_dict(self):
        """測試處理空字典."""
        data = {}
        result = process_data(data)
        assert "找到 0 個鍵" in result
        assert "不包含巢狀結構" in result

    def test_process_data_invalid_input(self):
        """測試無效輸入."""
        with pytest.raises(ValueError, match="資料必須是字典格式"):
            process_data("not a dict")


class TestCalculateSum:
    """測試 calculate_sum 函數."""

    def test_calculate_sum_positive_numbers(self):
        """測試正數總和."""
        assert calculate_sum([1, 2, 3, 4, 5]) == 15

    def test_calculate_sum_mixed_numbers(self):
        """測試混合正負數總和."""
        assert calculate_sum([1, -2, 3, -4, 5]) == 3

    def test_calculate_sum_empty_list(self):
        """測試空列表總和."""
        assert calculate_sum([]) == 0

    def test_calculate_sum_single_number(self):
        """測試單一數字總和."""
        assert calculate_sum([42]) == 42


class TestIsEven:
    """測試 is_even 函數."""

    def test_is_even_positive_even(self):
        """測試正偶數."""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(100) is True

    def test_is_even_positive_odd(self):
        """測試正奇數."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False

    def test_is_even_zero(self):
        """測試零."""
        assert is_even(0) is True

    def test_is_even_negative_numbers(self):
        """測試負數."""
        assert is_even(-2) is True
        assert is_even(-3) is False
