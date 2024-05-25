import yaml
from jinja2 import Environment, FileSystemLoader

try:
    # Load data from YAML file
    with open('data.yml') as f:
        data = yaml.safe_load(f)
except Exception as e:
    print(f"Error loading data.yml: {e}")
    exit(1)

try:
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('vhosts.j2')

    # Render template using data and write to vhosts.conf
    with open('vhosts.conf', 'w') as f:
        f.write(template.render(data))
except Exception as e:
    print(f"Error rendering template or writing to file: {e}")
    exit(1)