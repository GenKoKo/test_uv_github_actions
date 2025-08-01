#!/usr/bin/env python3
"""主程式模組 - 示範基本功能供 GitHub Actions 測試使用."""

import click
from .utils import fetch_data, process_data


@click.command()
@click.option('--name', default='World', help='要問候的名字')
@click.option('--count', default=1, help='重複次數')
def hello(name: str, count: int) -> None:
    """簡單的問候程式."""
    for _ in range(count):
        click.echo(f'Hello {name}!')


@click.command()
@click.option('--url', default='https://httpbin.org/json', help='要取得資料的 URL')
def fetch(url: str) -> None:
    """從 URL 取得資料並處理."""
    try:
        data = fetch_data(url)
        result = process_data(data)
        click.echo(f"處理結果: {result}")
    except Exception as e:
        click.echo(f"錯誤: {e}", err=True)
        raise


@click.group()
def cli() -> None:
    """GitHub Actions 練習程式."""
    pass


cli.add_command(hello)
cli.add_command(fetch)


if __name__ == '__main__':
    cli()