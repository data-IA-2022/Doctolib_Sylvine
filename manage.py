#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def run_custom_command():
    """Function to run the custom command."""
    os.system('python manage.py monitor')

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doctolibbydjango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # # Check if the 'runserver' command is being used
    # if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
    #     # Create a new thread in the new process to run the custom command
    #     from threading import Thread
    #     t = Thread(target=run_custom_command)
    #     t.start()

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()