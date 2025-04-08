# Add 'tracker' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'tracker',
]

# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit',
    }
}

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]

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