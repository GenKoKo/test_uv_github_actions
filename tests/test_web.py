"""測試網頁模組."""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch, Mock

import pytest

from src.github_actions_practice.web import generate_html_report, create_project_report


class TestGenerateHtmlReport:
    """測試 generate_html_report 函數."""
    
    def test_generate_html_report_basic(self):
        """測試基本 HTML 報告生成."""
        test_data = {
            'python_version': '3.11',
            'test_count': 10,
            'coverage': 85,
            'build_time': '2024-01-01 12:00:00',
            'git_commit': 'abc12345',
            'git_branch': 'main',
            'api_result': 'Test result',
            'timestamp': '2024-01-01 12:00:00 UTC'
        }
        
        html = generate_html_report(test_data)
        
        assert '<!DOCTYPE html>' in html
        assert 'GitHub Actions Practice' in html
        assert 'Python 3.11' in html
        assert '10 個測試通過' in html
        assert '85%' in html
        assert 'abc12345' in html
        assert 'main' in html
        assert 'Test result' in html
    
    def test_generate_html_report_with_special_characters(self):
        """測試包含特殊字符的 HTML 報告生成."""
        test_data = {
            'python_version': '3.9',
            'test_count': 5,
            'coverage': 100,
            'build_time': '2024-01-01',
            'git_commit': 'def67890',
            'git_branch': 'feature/test',
            'api_result': 'Success: 找到 3 個鍵，包含巢狀結構',
            'timestamp': '2024-01-01 UTC'
        }
        
        html = generate_html_report(test_data)
        
        assert 'feature/test' in html
        assert '找到 3 個鍵' in html
        assert '100%' in html


class TestCreateProjectReport:
    """測試 create_project_report 函數."""
    
    @patch('src.github_actions_practice.web.fetch_data')
    @patch('src.github_actions_practice.web.process_data')
    def test_create_project_report_success(self, mock_process_data, mock_fetch_data):
        """測試成功建立專案報告."""
        # 設置 mock
        mock_fetch_data.return_value = {"test": "data"}
        mock_process_data.return_value = "找到 1 個鍵，不包含巢狀結構"
        
        with tempfile.TemporaryDirectory() as temp_dir:
            # 改變工作目錄到臨時目錄
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                create_project_report()
                
                # 檢查檔案是否被建立
                docs_dir = Path('docs')
                assert docs_dir.exists()
                
                index_file = docs_dir / 'index.html'
                assert index_file.exists()
                
                # 檢查檔案內容
                content = index_file.read_text(encoding='utf-8')
                assert 'GitHub Actions Practice' in content
                assert '找到 1 個鍵' in content
                
            finally:
                os.chdir(original_cwd)
    
    @patch('src.github_actions_practice.web.fetch_data')
    def test_create_project_report_api_failure(self, mock_fetch_data):
        """測試 API 呼叫失敗時的報告建立."""
        # 設置 mock 拋出異常
        mock_fetch_data.side_effect = Exception("Network error")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                create_project_report()
                
                # 檢查檔案是否被建立
                index_file = Path('docs/index.html')
                assert index_file.exists()
                
                # 檢查錯誤訊息是否包含在內容中
                content = index_file.read_text(encoding='utf-8')
                assert 'API 呼叫失敗' in content
                assert 'Network error' in content
                
            finally:
                os.chdir(original_cwd)
    
    @patch.dict(os.environ, {'GITHUB_SHA': 'abcdef123456789', 'GITHUB_REF_NAME': 'develop'})
    @patch('src.github_actions_practice.web.fetch_data')
    @patch('src.github_actions_practice.web.process_data')
    def test_create_project_report_with_github_env(self, mock_process_data, mock_fetch_data):
        """測試使用 GitHub 環境變數的報告建立."""
        mock_fetch_data.return_value = {"test": "data"}
        mock_process_data.return_value = "Test result"
        
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                create_project_report()
                
                index_file = Path('docs/index.html')
                content = index_file.read_text(encoding='utf-8')
                
                # 檢查 GitHub 環境變數是否被正確使用
                assert 'abcdef12' in content  # 前8個字符
                assert 'develop' in content
                
            finally:
                os.chdir(original_cwd)