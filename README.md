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
# 問候命令
uv run python -m src.github_actions_practice.main hello --name "你的名字"

# 取得並處理 API 資料
uv run python -m src.github_actions_practice.main fetch --url "https://httpbin.org/json"

# 生成專案報告網頁
uv run python -m src.github_actions_practice.main report
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
4. **Deploy** (`deploy.yml`) - 自動部署到 GitHub Pages
5. **Schedule** (`schedule.yml`) - 定時任務和健康檢查

## 🌐 線上展示

專案會自動部署到 GitHub Pages，你可以在以下位置查看：

-   **專案報告**: `https://your-username.github.io/github-actions-practice-uv/`
-   **測試覆蓋率報告**: `https://your-username.github.io/github-actions-practice-uv/coverage/`

### 本地預覽

```bash
# 生成報告
make run-report

# 啟動本地伺服器預覽
make serve-docs
# 然後在瀏覽器開啟 http://localhost:8000
```

## 學習目標

-   ✅ 使用 uv 管理 Python 專案依賴
-   ✅ 設置 GitHub Actions CI/CD 流程
-   ✅ 自動化測試、程式碼檢查和發布
-   ✅ 練習不同的觸發條件和工作流程
-   ✅ 自動生成和部署專案文件
-   ✅ 使用 GitHub Pages 展示專案成果
-   ✅ 整合測試覆蓋率報告
-   ✅ 實現完整的 DevOps 流程

## 🎯 展示的 GitHub Actions 功能

### 1. 持續整合 (CI)

-   多版本 Python 測試 (3.9, 3.10, 3.11, 3.12)
-   自動化測試執行
-   程式碼品質檢查 (Black, Flake8, MyPy)
-   測試覆蓋率報告

### 2. 持續部署 (CD)

-   自動建置專案套件
-   GitHub Pages 自動部署
-   專案報告自動生成
-   測試覆蓋率視覺化

### 3. 自動化任務

-   定時依賴檢查
-   健康檢查
-   安全性掃描
-   自動化發布

### 4. 工作流程觸發

-   Push 觸發
-   Pull Request 觸發
-   定時觸發 (Cron)
-   手動觸發
-   工作流程完成觸發
