.PHONY: install test lint format clean build run help

help: ## 顯示說明
	@echo "可用的命令："
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## 安裝依賴
	uv sync --extra dev

test: ## 執行測試
	uv run pytest --cov=src --cov-report=term-missing

test-verbose: ## 執行詳細測試
	uv run pytest -v --cov=src --cov-report=term-missing --cov-report=html

lint: ## 執行程式碼檢查
	uv run flake8 src tests
	uv run mypy src

format: ## 格式化程式碼
	uv run black src tests

format-check: ## 檢查程式碼格式
	uv run black --check --diff src tests

clean: ## 清理暫存檔案
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/
	rm -rf build/ dist/ *.egg-info/

build: ## 建立套件
	uv build

run: ## 執行主程式
	uv run python -m src.github_actions_practice.main

run-hello: ## 執行 hello 命令
	uv run python -m src.github_actions_practice.main hello

run-fetch: ## 執行 fetch 命令
	uv run python -m src.github_actions_practice.main fetch

dev-setup: install ## 設置開發環境
	@echo "開發環境設置完成！"
	@echo "執行 'make help' 查看可用命令"