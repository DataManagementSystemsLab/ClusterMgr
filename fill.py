from jinja2 import Environment, FileSystemLoader

# Define the path to the template file and output file
template_path = "vm.tmpl"
output_path = "output.txt"

import mysql.connector
#fix identation
# Establish connections to the source and target databases

source_db_config = {
    'host': '127.0.0.1',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster',
}
source_db = mysql.connector.connect(**source_db_config)
source_cursor = source_db.cursor()
source_cursor.execute("select id as indx, ipaddr as ip, memory*1024*1024 as memory, vcpu,macaddr as mac,hostname from vms;")

columns = [column[0] for column in source_cursor.description]

result_set = source_cursor.fetchall()
data_as_dict = {"vms": [dict(zip(columns, row)) for row in result_set]}

print(data_as_dict)


# Create cursors


# Initialize Jinja2 environment with the template folder
env = Environment(loader=FileSystemLoader("."))

# Load the template
template = env.get_template(template_path)

# Render the template with data
filled_template = template.render(data_as_dict)

# Write the filled template to the output file
with open(output_path, "w") as output_file:
    output_file.write(filled_template)

print(f"Template filled and saved to {output_path}")
