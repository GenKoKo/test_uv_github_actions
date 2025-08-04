# 🚀 GitHub Actions Practice with uv and Python

這是一個完整的 Python 專案，展示如何使用 **uv** 作為包管理器，並建立完整的 **GitHub Actions CI/CD 流程**。專案包含自動化測試、程式碼品質檢查、自動部署等現代 DevOps 實踐。

## 📊 專案狀態

![CI Pipeline](https://github.com/GenKoKo/test_uv_github_actions/actions/workflows/ci.yml/badge.svg)
![Code Quality](https://github.com/GenKoKo/test_uv_github_actions/actions/workflows/lint.yml/badge.svg)
![Deploy](https://github.com/GenKoKo/test_uv_github_actions/actions/workflows/deploy.yml/badge.svg)

-   **測試覆蓋率**: 89%
-   **測試數量**: 25 個測試
-   **支援 Python 版本**: 3.9, 3.10, 3.11, 3.12
-   **程式碼品質工具**: Black, Flake8, MyPy

## 📁 專案結構

```
├── src/
│   └── github_actions_practice/
│       ├── __init__.py          # 套件初始化
│       ├── main.py              # CLI 主程式
│       ├── utils.py             # 工具函數
│       └── web.py               # 網頁報告生成
├── tests/
│   ├── __init__.py
│   ├── test_main.py             # CLI 測試
│   ├── test_utils.py            # 工具函數測試
│   └── test_web.py              # 網頁功能測試
├── .github/
│   └── workflows/
│       ├── ci.yml               # 持續整合流程
│       ├── deploy.yml           # GitHub Pages 部署
│       ├── lint.yml             # 程式碼品質檢查
│       ├── release.yml          # 自動化發布
│       └── schedule.yml         # 定時任務
├── docs/                        # 自動生成的文件
├── htmlcov/                     # 測試覆蓋率報告
├── Makefile                     # 常用命令快捷方式
├── pyproject.toml               # 專案配置
├── uv.lock                      # 依賴鎖定檔案
└── README.md
```

## 🛠️ 安裝與使用

### 前置需求

-   Python 3.9+
-   [uv](https://docs.astral.sh/uv/) 包管理器

### 快速開始

```bash
# 1. 複製專案
git clone https://github.com/GenKoKo/test_uv_github_actions.git
cd test_uv_github_actions

# 2. 安裝依賴（包含開發工具）
uv sync --extra dev

# 3. 執行測試確認環境正常
uv run pytest
```

### 🎯 主要功能

#### CLI 命令

```bash
# 問候功能
uv run python -m src.github_actions_practice.main hello --name "你的名字" --count 3

# API 資料取得與處理
uv run python -m src.github_actions_practice.main fetch --url "https://httpbin.org/json"

# 生成專案報告網頁
uv run python -m src.github_actions_practice.main report
```

#### 使用 Makefile 快捷命令

```bash
# 開發環境設置
make dev-setup

# 執行測試
make test                    # 基本測試
make test-verbose           # 詳細測試 + HTML 覆蓋率報告

# 程式碼品質
make format                 # 自動格式化程式碼
make lint                   # 程式碼品質檢查

# 專案報告
make run-report            # 生成專案報告
make serve-docs            # 啟動本地文件伺服器

# 建置
make build                 # 建立 Python 套件
```

### 🧪 測試與品質檢查

```bash
# 執行完整測試套件（25 個測試）
uv run pytest --cov=src --cov-report=html --cov-report=term-missing

# 程式碼品質三步驟
uv run black src tests      # 1. 格式化程式碼
uv run flake8 src tests     # 2. 語法與風格檢查
uv run mypy src            # 3. 型別檢查
```

## ⚙️ GitHub Actions 工作流程

本專案展示了完整的 CI/CD 流程，包含 5 個自動化工作流程：

### 🔄 持續整合 (CI)

| 工作流程         | 檔案       | 觸發條件 | 功能                                                     |
| ---------------- | ---------- | -------- | -------------------------------------------------------- |
| **CI Pipeline**  | `ci.yml`   | Push, PR | 多版本測試 (Python 3.9-3.12)、建置套件                   |
| **Code Quality** | `lint.yml` | Push, PR | Black 格式化、Flake8 語法檢查、MyPy 型別檢查、安全性掃描 |

### 🚀 持續部署 (CD)

| 工作流程                   | 檔案          | 觸發條件              | 功能                                  |
| -------------------------- | ------------- | --------------------- | ------------------------------------- |
| **Deploy to GitHub Pages** | `deploy.yml`  | Push to main, CI 完成 | 自動生成專案報告、部署到 GitHub Pages |
| **Release**                | `release.yml` | Git tag (v\*)         | 自動建立 GitHub Release、發布到 PyPI  |

### ⏰ 自動化任務

| 工作流程            | 檔案           | 觸發條件                 | 功能                   |
| ------------------- | -------------- | ------------------------ | ---------------------- |
| **Scheduled Tasks** | `schedule.yml` | 每日 UTC 02:00、手動觸發 | 依賴安全檢查、健康檢查 |

## 🌐 線上展示

專案會自動部署到 GitHub Pages，展示完整的專案資訊：

-   **🏠 專案報告**: https://genkoko.github.io/test_uv_github_actions/
-   **📊 測試覆蓋率**: https://genkoko.github.io/test_uv_github_actions/coverage/

### 本地預覽

```bash
# 生成最新報告
make run-report

# 啟動本地伺服器 (http://localhost:8000)
make serve-docs
```

## 🎯 學習目標與成果

這個專案展示了現代 Python 開發的最佳實踐：

### ✅ 已實現的功能

| 類別           | 功能                           | 工具/技術           |
| -------------- | ------------------------------ | ------------------- |
| **包管理**     | 現代 Python 包管理             | uv, pyproject.toml  |
| **程式碼品質** | 自動格式化、語法檢查、型別檢查 | Black, Flake8, MyPy |
| **測試**       | 單元測試、覆蓋率報告           | pytest, pytest-cov  |
| **CI/CD**      | 多版本測試、自動部署           | GitHub Actions      |
| **文件**       | 自動生成專案報告               | 自製 HTML 生成器    |
| **部署**       | 靜態網站自動部署               | GitHub Pages        |

### 🚀 展示的 DevOps 實踐

#### 1. **持續整合 (Continuous Integration)**

-   ✅ 多版本 Python 測試矩陣 (3.9, 3.10, 3.11, 3.12)
-   ✅ 自動化測試執行 (25 個測試，89% 覆蓋率)
-   ✅ 程式碼品質門檻 (格式化、語法、型別檢查)
-   ✅ 安全性掃描

#### 2. **持續部署 (Continuous Deployment)**

-   ✅ 自動建置 Python 套件
-   ✅ GitHub Pages 自動部署
-   ✅ 專案報告自動生成和更新
-   ✅ 測試覆蓋率視覺化

#### 3. **自動化與監控**

-   ✅ 定時依賴安全檢查
-   ✅ 健康檢查自動化
-   ✅ 多種觸發條件 (Push, PR, Schedule, Manual)
-   ✅ 工作流程間的依賴管理

## 🛠️ 技術棧

### 核心技術

-   **Python 3.9+** - 程式語言
-   **uv** - 現代 Python 包管理器
-   **pytest** - 測試框架
-   **Click** - CLI 框架

### 開發工具

-   **Black** - 程式碼格式化
-   **Flake8** - 語法和風格檢查
-   **MyPy** - 靜態型別檢查
-   **pytest-cov** - 測試覆蓋率

### CI/CD 平台

-   **GitHub Actions** - 自動化流程
-   **GitHub Pages** - 靜態網站託管

## 📚 適合學習的對象

-   🐍 想學習現代 Python 開發流程的開發者
-   🔄 希望了解 CI/CD 實踐的工程師
-   🚀 需要建立自動化測試和部署的團隊
-   📊 想要整合程式碼品質檢查的專案

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

### 開發流程

1. Fork 這個專案
2. 建立功能分支: `git checkout -b feature/amazing-feature`
3. 提交變更: `git commit -m 'Add amazing feature'`
4. 推送分支: `git push origin feature/amazing-feature`
5. 開啟 Pull Request

### 程式碼規範

-   使用 `make format` 格式化程式碼
-   使用 `make lint` 檢查程式碼品質
-   使用 `make test` 確保測試通過
-   為新功能添加測試

## 📄 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 🙏 致謝

-   [uv](https://github.com/astral-sh/uv) - 現代 Python 包管理器
-   [GitHub Actions](https://github.com/features/actions) - CI/CD 平台
-   [pytest](https://pytest.org/) - Python 測試框架

---

⭐ 如果這個專案對你有幫助，請給個 Star！
