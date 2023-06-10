def generate_leaf_svg(filename):
    # Define the SVG header and dimensions
    svg_header = "<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'>"

    # Define the leaf shape using SVG path elements
    leaf_shape = "<path d='M100,100 C150,50 200,150 250,100 C100,100 300,250 100,100' stroke='black' fill='none'/>"

    # # Define a second leaf shape that is rotated by 90 degrees
    # rotated_leaf_shape = "<path d='M100 100 Q 75 150, 100 200 Q 125 150, 100 100 Z' />"

    # Combine the header and shapes into a single string
    svg_content = svg_header + leaf_shape + "</svg>"

    # Write the SVG content to the specified file
    with open(filename, "w") as f:
        f.write(svg_content)

# Example usage:
generate_leaf_svg("leaf.svg")

# Example usage:
generate_leaf_svg("leaf.svg")
