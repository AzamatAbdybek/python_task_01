import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import os

def main():
    try:
        # Check if data.yml exists and is readable
        if not os.path.isfile('data.yml'):
            sys.exit(1)
        if not os.access('data.yml', os.R_OK):
            sys.exit(1)

        # Check if vhosts.j2 exists and is readable
        if not os.path.isfile('vhosts.j2'):
            sys.exit(1)
        if not os.access('vhosts.j2', os.R_OK):
            sys.exit(1)

        # Load the YAML data
        with open('data.yml', 'r') as f:
            data = yaml.safe_load(f)

        # Setup Jinja2 environment
        env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('vhosts.j2')

        # Render template using data and write to vhosts.conf
        rendered_conf = template.render(vhosts=data['vhosts'])
        with open('vhosts.conf', 'w') as f:
            f.write(rendered_conf)

        # Verify the output file is written and readable
        if not os.path.isfile('vhosts.conf') or not os.access('vhosts.conf', os.R_OK):
            sys.exit(1)

    except yaml.YAMLError:
        sys.exit(1)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()