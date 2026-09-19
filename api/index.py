import os
import subprocess

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventUp.settings')

try:
	subprocess.run(
		['python', 'manage.py', 'collectstatic', '--noinput'],
		check=True,
		cwd=os.path.dirname(os.path.dirname(__file__)),
	)
except Exception as error:
	print(f'collectstatic failed: {error}')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
