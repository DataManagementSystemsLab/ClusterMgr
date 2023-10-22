from jinja2 import Environment, FileSystemLoader

# Define the path to the template file and output file
template_path = "vm.tmpl"
output_path = "output.txt"

data = {
    "vms": [
        {
            "name": "my_vm",
            "indx": 1,
            "ip": "10.100.14.1",
            "mac": "ae:52:0a:b0:14:01",
            "memory": 4096,
            "vcpu": 4
        },
        {
            "name": "my_vm2",
            "indx": 2,
            "ip": "10.100.14.2",
            "mac": "ae:52:0a:b0:14:02",
            "memory": 4096,
            "vcpu": 4
        }
    ]
}

# Initialize Jinja2 environment with the template folder
env = Environment(loader=FileSystemLoader("."))

# Load the template
template = env.get_template(template_path)

# Render the template with data
filled_template = template.render(data)

# Write the filled template to the output file
with open(output_path, "w") as output_file:
    output_file.write(filled_template)

print(f"Template filled and saved to {output_path}")
