import os
import settings
import pandas as pd
import webbrowser


# Read the data-set into a data table using Pandas
data_table = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "endangered_species.csv"))

# Create a web page view of the data for easy viewing
html = data_table[0:250].to_html()

# Save the html to a temporary file
with open(os.path.join(settings.PROCESSED_DIR, "endangered_species.html"), "w") as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath(os.path.join(settings.PROCESSED_DIR, "endangered_species.html"))
webbrowser.open("file://{}".format(full_filename))
