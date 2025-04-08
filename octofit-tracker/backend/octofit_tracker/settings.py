# Add 'tracker' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'tracker',
]

# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # Database engine for MongoDB
        'NAME': 'octofit_db',  # Name of the database
    }
}

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Insert CORS middleware at the top
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']