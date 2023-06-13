#!/bin/sh

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Check if the user 'denver' exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='denver').exists())" | python manage.py shell | grep -q "True"

# Create default user if it doesn't exist
if [ $? -ne 0 ]; then
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('denver', 'admin@example.com', 'denver*123')" | python manage.py shell
fi

# Start the web server
exec "$@"
