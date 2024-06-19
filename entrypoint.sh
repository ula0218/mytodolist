#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Create .env file with database configuration
cat << EOF > .env
DB_NAME=test1
DB_USER=root
DB_PASSWORD=123
DB_HOST=mydb
DB_PORT=3306
EOF

# Run database migrations
poetry run python manage.py migrate

# Start the Django development server
poetry run python manage.py runserver 0.0.0.0:80
