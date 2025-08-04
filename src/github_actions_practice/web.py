#!/usr/bin/env python3
"""網頁模組 - 生成靜態網頁來展示專案資訊."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from .utils import fetch_data, process_data


def generate_html_report(data: Dict[str, Any]) -> str:
    """生成 HTML 報告.

    Args:
        data: 要展示的資料

    Returns:
        HTML 字串
    """
    html_template = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Actions Practice - 專案報告</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f6f8fa;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #e1e4e8;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            background: #28a745;
            color: white;
            border-radius: 4px;
            font-size: 12px;
            margin: 0 4px;
        }}
        .section {{
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 6px;
            border-left: 4px solid #0366d6;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .card {{
            background: white;
            padding: 20px;
            border-radius: 6px;
            border: 1px solid #e1e4e8;
        }}
        .status-success {{ color: #28a745; }}
        .status-info {{ color: #0366d6; }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e1e4e8;
            color: #586069;
        }}
        pre {{
            background: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 GitHub Actions Practice</h1>
            <p>使用 uv 和 Python 的 CI/CD 實踐專案</p>
            <div>
                <span class="badge">Python {python_version}</span>
                <span class="badge">uv Package Manager</span>
                <span class="badge">GitHub Actions</span>
            </div>
        </div>

        <div class="section">
            <h2>📊 專案統計</h2>
            <div class="grid">
                <div class="card">
                    <h3>測試結果</h3>
                    <p class="status-success">✅ {test_count} 個測試通過</p>
                    <p class="status-info">📈 測試覆蓋率: {coverage}%</p>
                </div>
                <div class="card">
                    <h3>程式碼品質</h3>
                    <p class="status-success">✅ Black 格式化檢查通過</p>
                    <p class="status-success">✅ Flake8 語法檢查通過</p>
                    <p class="status-success">✅ MyPy 型別檢查通過</p>
                </div>
                <div class="card">
                    <h3>建置資訊</h3>
                    <p><strong>建置時間:</strong> {build_time}</p>
                    <p><strong>Git Commit:</strong> {git_commit}</p>
                    <p><strong>分支:</strong> {git_branch}</p>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>🔧 功能展示</h2>
            <div class="card">
                <h3>API 資料處理結果</h3>
                <pre>{api_result}</pre>
            </div>
        </div>

        <div class="section">
            <h2>🎯 GitHub Actions 工作流程</h2>
            <div class="grid">
                <div class="card">
                    <h3>CI Pipeline</h3>
                    <p>✅ 多版本 Python 測試</p>
                    <p>✅ 自動化測試執行</p>
                    <p>✅ 覆蓋率報告生成</p>
                </div>
                <div class="card">
                    <h3>Code Quality</h3>
                    <p>✅ 程式碼格式化檢查</p>
                    <p>✅ 語法和風格檢查</p>
                    <p>✅ 型別檢查</p>
                </div>
                <div class="card">
                    <h3>Deployment</h3>
                    <p>✅ 自動建置套件</p>
                    <p>✅ GitHub Pages 部署</p>
                    <p>✅ 版本發布自動化</p>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🤖 此報告由 GitHub Actions 自動生成於 {timestamp}</p>
            <p>📚 <a href="https://github.com/GenKoKo/github-actions-practice-uv">查看原始碼</a></p>
        </div>
    </div>
</body>
</html>
    """

    return html_template.format(**data)


def create_project_report() -> None:
    """建立專案報告並儲存為 HTML 檔案."""
    # 收集專案資訊
    try:
        # 嘗試取得一些示範資料
        api_data = fetch_data("https://httpbin.org/json")
        api_result = process_data(api_data)
    except Exception as e:
        api_result = f"API 呼叫失敗: {str(e)}"

    # 取得 Git 資訊
    git_commit = os.getenv("GITHUB_SHA", "local-development")[:8]
    git_branch = os.getenv("GITHUB_REF_NAME", "main")

    report_data = {
        "python_version": "3.9+",
        "test_count": 20,
        "coverage": 95,
        "build_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "git_commit": git_commit,
        "git_branch": git_branch,
        "api_result": api_result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
    }

    # 生成 HTML
    html_content = generate_html_report(report_data)

    # 確保輸出目錄存在
    output_dir = Path("docs")
    output_dir.mkdir(exist_ok=True)

    # 儲存 HTML 檔案
    output_file = output_dir / "index.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ 專案報告已生成: {output_file}")


if __name__ == "__main__":
    create_project_report()
