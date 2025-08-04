"""工具函數模組."""

import requests
from typing import Dict, Any


def fetch_data(url: str) -> Dict[str, Any]:
    """從指定 URL 取得 JSON 資料.

    Args:
        url: 要取得資料的 URL

    Returns:
        解析後的 JSON 資料

    Raises:
        requests.RequestException: 當請求失敗時
        ValueError: 當回應不是有效的 JSON 時
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()  # type: ignore[no-any-return]


def process_data(data: Dict[str, Any]) -> str:
    """處理取得的資料.

    Args:
        data: 要處理的資料字典

    Returns:
        處理後的結果字串
    """
    if not isinstance(data, dict):
        raise ValueError("資料必須是字典格式")

    # 簡單的資料處理邏輯
    keys_count = len(data.keys())
    has_nested = any(isinstance(v, (dict, list)) for v in data.values())

    return f"找到 {keys_count} 個鍵，{'包含' if has_nested else '不包含'}巢狀結構"


def calculate_sum(numbers: list[int]) -> int:
    """計算數字列表的總和.

    Args:
        numbers: 整數列表

    Returns:
        總和
    """
    return sum(numbers)


def is_even(number: int) -> bool:
    """檢查數字是否為偶數.

    Args:
        number: 要檢查的數字

    Returns:
        如果是偶數回傳 True，否則回傳 False
    """
    return number % 2 == 0
