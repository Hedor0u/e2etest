@echo off
cd /d "%~dp0"

if not exist "env" (
    python -m venv env
)

call env\Scripts\activate

pip install -r requirements.txt

pytest tests\test_index_page.py

pause

deactivate