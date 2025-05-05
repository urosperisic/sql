git config --global user.name "new_username"
git config --global user.email "your@email.com"
[ Credential Manager - Windows ]

git reset --soft HEAD~1
git restore --staged .

--------------------

pip list

python -m venv venv
venv\Scripts\activate
venv\Scripts\deactivate

pip freeze > requirements.txt
pip install -r requirements.txt

____________________

pip install pytest
pip install pytest-cov

pytest
pytest -s
pytest --cov=app_test
pytest --cov=app_test --cov-report=term-missing

--------------------