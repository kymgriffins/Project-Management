# Create a virtual environment
echo "Creating a virtual environment..."
python -m pip install wheel setuptools pip --upgrade
python3 -m pip install wheel setuptools pip --upgrade
py -m pip install wheel setuptools pip --upgrade
python3.9 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear
echo "BUILD END"
