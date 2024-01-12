
from django.core.management.base import BaseCommand
import pandas as pd
from application.models import medData  # Replace 'YourModel' with the actual model name

class Command(BaseCommand):
    help = 'Import data from a table into a Pandas DataFrame'

    def handle(self, *args, **options):
        data = medData.objects.values()  # Replace 'YourModel' with the actual model name
        df = pd.DataFrame.from_records(data)

        # Now you have your data in a Pandas DataFrame (df)
        # You can perform further operations on the DataFrame or export it to a CSV, Excel, etc.
        print(df.head())