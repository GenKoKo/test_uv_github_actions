# GitHub Actions Practice with uv and Python

這是一個用來練習 GitHub Actions 的 Python 專案，使用 uv 作為包管理器。

## 專案結構

```
├── src/
│   └── github_actions_practice/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── release.yml
│       └── lint.yml
├── pyproject.toml
├── README.md
└── .gitignore
```

## 安裝與使用

### 使用 uv 安裝依賴

```bash
# 安裝專案依賴
uv sync

# 安裝開發依賴
uv sync --extra dev
```

### 執行程式

```bash
# 執行主程式
uv run python -m src.github_actions_practice.main

# 或者使用 uv run
uv run src/github_actions_practice/main.py
```

### 執行測試

```bash
# 執行所有測試
uv run pytest

# 執行測試並顯示覆蓋率
uv run pytest --cov=src --cov-report=term-missing
```

### 程式碼格式化與檢查

```bash
# 格式化程式碼
uv run black src tests

# 檢查程式碼風格
uv run flake8 src tests

# 型別檢查
uv run mypy src
```

## GitHub Actions 工作流程

這個專案包含以下 GitHub Actions 工作流程：

1. **CI Pipeline** (`ci.yml`) - 在每次 push 和 PR 時執行測試
2. **Linting** (`lint.yml`) - 程式碼風格和品質檢查
3. **Release** (`release.yml`) - 自動化發布流程

## 學習目標

-   使用 uv 管理 Python 專案依賴
-   設置 GitHub Actions CI/CD 流程
-   自動化測試、程式碼檢查和發布
-   練習不同的觸發條件和工作流程
