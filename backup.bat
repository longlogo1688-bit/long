@echo off
chcp 65001 >nul
:: 自动备份脚本 - OpenClaw Workspace
:: 备份到指定目录

set "SOURCE=C:\Users\Administrator\.openclaw-zero\workspace"
set "BACKUP_DIR=D:\OpenClaw-Backup"
set "DATE=%date:~0,4%%date:~5,2%%date:~8,2%"
set "TIME=%time:~0,2%%time:~3,2%%time:~6,2%"
set "TIME=%TIME: =0%"
set "BACKUP_NAME=openclaw-backup-%DATE%-%TIME%"

echo ========================================
echo OpenClaw 自动备份工具
echo 备份时间: %DATE% %TIME%
echo ========================================

:: 检查备份目录是否存在
if not exist "%BACKUP_DIR%" (
    echo 创建备份目录: %BACKUP_DIR%
    mkdir "%BACKUP_DIR%"
)

:: 创建本次备份目录
set "TARGET=%BACKUP_DIR%\%BACKUP_NAME%"
mkdir "%TARGET%"

echo.
echo 正在备份文件...
echo 源目录: %SOURCE%
echo 目标目录: %TARGET%
echo.

:: 使用 xcopy 备份文件（排除 doubao-free-api 子模块）
xcopy "%SOURCE%\*" "%TARGET%\" /E /I /H /Y /EXCLUDE:%~dp0backup-exclude.txt 2>nul

if %errorlevel% == 0 (
    echo.
    echo ========================================
    echo 备份成功完成！
    echo 备份位置: %TARGET%
    echo ========================================
) else (
    echo.
    echo ========================================
    echo 备份完成，可能有部分文件被跳过
    echo 备份位置: %TARGET%
    echo ========================================
)

:: 清理旧备份（保留最近10个）
echo.
echo 清理旧备份...
for /f "skip=10 delims=" %%a in ('dir /b /ad /o-d "%BACKUP_DIR%\openclaw-backup-*"') do (
    echo 删除旧备份: %%a
    rmdir /s /q "%BACKUP_DIR%\%%a"
)

echo.
echo 按任意键退出...
pause >nul
