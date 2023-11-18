# Create a virtual environment
echo "Creating a virtual environment..."

python3.9 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear
echo "BUILD END"
