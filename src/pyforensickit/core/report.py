from jinja2 import Environment, FileSystemLoader
import os
from weasyprint import HTML

# Correctly construct the template directory path
# TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../templates"))


def generate_report(
    output_html,
    output_pdf=None,
    case=None,
    metadata=None,
    hashes=None,
    timeline=None,
    integrity_verification=None
):
    # Load template
    # env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report_template.html")

    # Render HTML
    html_content = template.render(
        case=case,
        metadata=metadata,
        hashes=hashes,
        timeline=timeline,
        integrity_verification=integrity_verification
    )

    # Save HTML
    with open(output_html, "w") as f:
        f.write(html_content)

    print(f"[green]HTML report generated:[/green] {output_html}")

    # Optionally generate PDF
    if output_pdf:
        HTML(string=html_content).write_pdf(output_pdf)
        print(f"[green]PDF report generated:[/green] {output_pdf}")
