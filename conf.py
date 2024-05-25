import yaml
from jinja2 import Environment, FileSystemLoader

try:
    # Load data from YAML file
    with open('data.yml') as f:
        data = yaml.safe_load(f)
except Exception as error:
    print('Failed to load data.yml:', error)
    exit(1)

try:
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('vhosts.j2')
except Exception as error:
    print('Failed to load vhosts.j2 template:', error)
    exit(1)

try:
    # Render template using data and write to vhosts.conf
    with open('generated_vhosts.conf', 'w') as f:
        f.write(template.render(data))
except Exception as error:
    print('Failed to render template or write to generated_vhosts.conf:', error)
    exit(1)