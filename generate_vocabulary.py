import rdflib
from rdflib.namespace import RDF, RDFS, OWL
import os

def generate_vocabulary_for_file(ttl_file, output_dir):
    """Generates a Markdown vocabulary document for a single TTL file."""
    g = rdflib.Graph()
    try:
        g.parse(ttl_file, format="turtle")
    except Exception as e:
        print(f"Error parsing {ttl_file}: {e}")
        return

    # Extract a prefix for the ontology
    prefix = ""
    for p, n in g.namespaces():
        if "ns.slashlife.ai" in str(n):
            prefix = p
            break

    if not prefix:
        prefix = os.path.basename(ttl_file).split('.')[0]


    md_content = f"# Vocabulary for {prefix.capitalize()} Ontology\n\n"

    # --- Extract Classes ---
    classes = list(g.subjects(RDF.type, OWL.Class))
    if classes:
        md_content += "## Classes\n\n"
        md_content += "| Class | Definition |\n"
        md_content += "|:------|:-----------|\n"
        for cls in sorted(classes):
            label = g.value(cls, RDFS.label) or cls.split('#')[-1].split('/')[-1]
            comment = g.value(cls, RDFS.comment) or ""
            md_content += f"| `{prefix}:{label}` | {comment} |\n"
        md_content += "\n"

    # --- Extract Properties ---
    properties = list(g.subjects(RDF.type, OWL.ObjectProperty)) + list(g.subjects(RDF.type, OWL.DatatypeProperty))
    if properties:
        md_content += "## Properties\n\n"
        md_content += "| Property | Domain | Range | Definition |\n"
        md_content += "|:---------|:-------|:------|:-----------|\n"
        for prop in sorted(properties):
            label = g.value(prop, RDFS.label) or prop.split('#')[-1].split('/')[-1]
            domain = g.value(prop, RDFS.domain)
            range_ = g.value(prop, RDFS.range)
            comment = g.value(prop, RDFS.comment) or ""

            domain_str = f"`{prefix}:{g.value(domain, RDFS.label)}`" if domain else "N/A"
            range_str = f"`{prefix}:{g.value(range_, RDFS.label)}`" if range_ and isinstance(range_, rdflib.URIRef) else (str(range_).split('#')[-1] if range_ else "N/A")
            
            # Make range more readable for XSD types
            if "http://www.w3.org/2001/XMLSchema#" in str(range_):
                range_str = f"`xsd:{str(range_).split('#')[-1]}`"


            md_content += f"| `{prefix}:{label}` | {domain_str} | {range_str} | {comment} |\n"
        md_content += "\n"

    # Write to file
    output_filename = os.path.join(output_dir, f"{prefix}-vocabulary.md")
    with open(output_filename, "w") as f:
        f.write(md_content)
    print(f"Generated vocabulary for {ttl_file} at {output_filename}")


def main():
    """Main function to generate vocabulary for all ontology files."""
    ontology_dir = "ontologies"
    output_dir = "specs/vocabulary"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in sorted(os.listdir(ontology_dir)):
        if filename.endswith(".ttl"):
            ttl_file_path = os.path.join(ontology_dir, filename)
            generate_vocabulary_for_file(ttl_file_path, output_dir)

if __name__ == "__main__":
    main()
