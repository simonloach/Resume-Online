git fetch origin master
git reset --hard FETCH_HEAD
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 jinja.py
sudo cp -r html /resume-online