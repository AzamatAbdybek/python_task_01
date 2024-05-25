import yaml
from jinja2 import Environment, FileSystemLoader

# Load data from YAML file
try:
    with open('data.yml') as f:
        data = yaml.safe_load(f)
except Exception as err:
    print('Error while loading data from data.yml:', err)
    exit(1)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
try:
    template = env.get_template('vhosts.j2')
except Exception as err:
    print('Error while loading the vhosts.j2 template:', err)
    exit(1)

# Render template using data and write to vhosts.conf
try:
    with open('generated_vhosts.conf', 'w') as f:
        f.write(template.render(data))
except Exception as err:
    print('Error occurred while rendering the template or writing to generated_vhosts.conf:', err)
    exit(1)