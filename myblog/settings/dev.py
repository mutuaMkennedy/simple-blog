from .base import *

# For windows os to find GDAL installation
if os.name == 'nt':
    import platform
    OSGEO4W = r'C:\OSGeo4W'
    if '64' in platform.architecture()[0]:
        OSGEO4W += '64'
    assert os.path.isdir(OSGEO4W), 'Directory does not exist: ' + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r'\share\gdal'
    os.environ['PROJ_LIB'] = OSGEO4W + r'\share\proj'
    os.environ['PATH'] = OSGEO4W + r'\bin;' + os.environ['PATH']

GDAL_LIBRARY_PATH = r''+ config('GDAL_LIB_PATH')+'' # some\path\to\gdal.dll

DEBUG = config('DEBUG', cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}
