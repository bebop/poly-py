# Create base output directory
output_dir="poly"
mkdir -p $output_dir

# Get all subpackages and build them
go list github.com/bebop/poly/... | while read pkg; do
    # Create corresponding output directory structure

    pkg_path=${pkg#github.com/bebop/poly/}  # Remove module prefix

    mkdir -p "$output_dir/$pkg_path"
    
    # Build the package
    gopy build -output="$output_dir/$pkg_path" -vm=python3 "$pkg"
    
    # Create __init__.py for Python package
    touch "$output_dir/$pkg_path/__init__.py"
done


# Create root __init__.py
touch $output_dir/__init__.py