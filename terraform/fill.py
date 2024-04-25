from jinja2 import Environment, FileSystemLoader
import mysql.connector
import sys
# Define the path to the template file and output file
template_path = "vm.tmpl"
output_path = "output.txt"



def fill(config,loc):
    source_db = mysql.connector.connect(**source_db_config)
    source_cursor = source_db.cursor()
    source_cursor.execute(f"select  indx, ipaddr as ip, memory*1024 as memory, vcpu,macaddr as mac, hostname from vms where location = '{loc}';")

    columns = [column[0] for column in source_cursor.description]

    result_set = source_cursor.fetchall()
    data_as_dict = {"vms": [dict(zip(columns, row)) for row in result_set]}

    print(data_as_dict)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_path)

    filled_template = template.render(data_as_dict)
    return filled_template

if __name__ == "__main__":
    loc=sys.argv[1]
    source_db_config = {
    'host': '10.100.1.0',
    'user': 'owuser',
    'password': '',
    'database': 'owcluster',
    }
# Write the filled template to the output file
    with open(output_path, "w") as output_file:
        output_file.write(fill(source_db_config,loc))

    print(f"Template filled and saved to {output_path}")
