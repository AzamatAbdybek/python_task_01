import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import os

DATA_FILE = 'data.yml'
TEMPLATE_FILE = 'vhosts.j2'
OUTPUT_FILE = 'vhosts.conf'

def main():
    try:
        # Check if the files exist and can be opened/read
        for file in [DATA_FILE, TEMPLATE_FILE]:
            if not os.path.isfile(file) or not os.access(file, os.R_OK):
                sys.exit(1)

        # Load the YAML data
        with open(DATA_FILE, 'r') as f:
            data = yaml.safe_load(f)

        # Setup Jinja2 environment
        env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template(TEMPLATE_FILE)

        # Render template using data and write to the output file
        rendered_conf = template.render(vhosts=data['vhosts'])
        with open(OUTPUT_FILE, 'w') as f:
            f.write(rendered_conf)

        # Verify the output file is written and readable
        if not os.path.isfile(OUTPUT_FILE) or not os.access(OUTPUT_FILE, os.R_OK):
            sys.exit(1)

    except yaml.YAMLError:
        sys.exit(1)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()