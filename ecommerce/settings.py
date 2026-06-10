"""
Django settings for ecommerce project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# 🔐 SECURITY
SECRET_KEY = 'django-insecure-ag7w#^f8%*53($_9=uopt2osolj#@8@0l%$o47z)pulcw75j8d'

# ⚠️ Development mode (change to False during deployment)
DEBUG = True

ALLOWED_HOSTS = ["*"]   # add your domain when deploying


# 📦 APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store',
]


# 🧱 MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🌐 URL CONFIG
ROOT_URLCONF = 'ecommerce.urls'


# 🎨 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # FIXED (important)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🚀 WSGI
WSGI_APPLICATION = 'ecommerce.wsgi.application'


# 🗄 DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 🌍 INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'   # FIXED for India

USE_I18N = True

USE_TZ = True


# 📁 STATIC FILES (CSS, JS)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# 🖼 MEDIA FILES (images, uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 🔐 LOGIN SETTINGS
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# ⚡ OPTIONAL (good for future deployment)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'