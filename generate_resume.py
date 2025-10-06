#!/usr/bin/env python3
"""
generate_resume.py - minimal, reliable HTML generator

This script reads `resume_data.yaml`, renders `jinja_template.html` using Jinja2,
and writes the output to `html/index.html`.

Designed to be small and robust so it can be used in CI and locally.
"""
import os
from typing import Dict, Any

import yaml
from jinja2 import Template


def load_resume_data(path: str = "resume_data.yaml") -> Dict[str, Any]:
    """Load YAML resume data from file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_template(template_path: str, context: Dict[str, Any]) -> str:
    """Render the Jinja2 template with the provided context."""
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = Template(f.read())
    return tpl.render(**context)


def write_output(html: str, out_path: str = "html/index.html") -> None:
    """Write the rendered HTML to disk, creating directories as needed."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)


def main() -> None:
    data = load_resume_data()
    html = render_template("jinja_template.html", data)
    write_output(html)
    print("✅ index.html generated at html/index.html")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
generate_resume.py - minimal, reliable HTML generator

This script reads `resume_data.yaml`, renders `jinja_template.html` using Jinja2,
and writes the output to `html/index.html`.

Designed to be small and robust so it can be used in CI and locally.
"""
import os
from typing import Any, Dict

import yaml
from jinja2 import Template


def load_resume_data(path: str = "resume_data.yaml") -> Dict[str, Any]:
    """Load YAML resume data from file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_template(template_path: str, context: Dict[str, Any]) -> str:
    """Render the Jinja2 template with the provided context."""
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = Template(f.read())
    return tpl.render(**context)


def write_output(html: str, out_path: str = "html/index.html") -> None:
    """Write the rendered HTML to disk, creating directories as needed."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        #!/usr/bin/env python3
        """
        generate_resume.py - minimal, reliable HTML generator

        This script reads `resume_data.yaml`, renders `jinja_template.html` using Jinja2,
        and writes the output to `html/index.html`.

        Designed to be small and robust so it can be used in CI and locally.
        """
        import os
        from typing import Dict, Any

        import yaml
        from jinja2 import Template


        def load_resume_data(path: str = "resume_data.yaml") -> Dict[str, Any]:
            """Load YAML resume data from file."""
            with open(path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)


        def render_template(template_path: str, context: Dict[str, Any]) -> str:
            """Render the Jinja2 template with the provided context."""
            with open(template_path, "r", encoding="utf-8") as f:
                tpl = Template(f.read())
            return tpl.render(**context)


        def write_output(html: str, out_path: str = "html/index.html") -> None:
            """Write the rendered HTML to disk, creating directories as needed."""
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)


        def main() -> None:
            data = load_resume_data()
            html = render_template("jinja_template.html", data)
            write_output(html)
            print("✅ index.html generated at html/index.html")


        if __name__ == "__main__":
            main()