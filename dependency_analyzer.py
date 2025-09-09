import os
import re
import glob
from collections import defaultdict

# Regex based on the plan, but adapted for re.finditer and multiline content
# 1. `import <module>` or `import <module> as <alias>`
IMPORT_RE = re.compile(r"^\s*import\s+([\w.]+)(?:\s+as\s+\w+)?", re.MULTILINE)
# 2. `from <module> import <member1>, <member2> as <alias2>, ...`
# This is complex. We'll capture the module and the full members string.
FROM_IMPORT_RE = re.compile(r"^\s*from\s+([\w.]+)\s+import\s+(.*)", re.MULTILINE)

def clean_member(member_str):
    """Cleans and extracts the base member name from an import string."""
    member_str = member_str.strip()
    # Remove comments
    if '#' in member_str:
        member_str = member_str.split('#', 1)[0].strip()
    # Remove alias
    if ' as ' in member_str:
        member_str = member_str.split(' as ', 1)[0].strip()
    return member_str

def analyze_dependencies(root_dir):
    """
    Analyzes Python files in a directory to find API-level dependencies.
    """
    print(f"Starting analysis in root directory: {root_dir}")
    py_files = glob.glob(os.path.join(root_dir, '**', '*.py'), recursive=True)
    
    # Filter out virtual environments and other non-project code
    exclude_dirs = ['.venv', '.git', '__pycache__', 'site-packages', 'dist', 'build', 'detectron2/projects']
    original_count = len(py_files)
    py_files = [f for f in py_files if not any(f"{os.sep}{d}{os.sep}" in f or f.startswith(d + os.sep) for d in exclude_dirs)]
    print(f"Found {original_count} Python files, analyzing {len(py_files)} after filtering.")

    api_usage = defaultdict(lambda: defaultdict(list))

    for file_path in py_files:
        rel_path = os.path.relpath(file_path, root_dir)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except (IOError, UnicodeDecodeError) as e:
            print(f"Warning: Could not read file {rel_path}: {e}")
            continue

        # --- Handle `import module` ---
        for match in IMPORT_RE.finditer(content):
            module = match.group(1)
            api_usage[module]["*module*"].append(rel_path)

        # --- Handle `from module import ...` ---
        for match in FROM_IMPORT_RE.finditer(content):
            module, members_group = match.groups()
            
            # This is a heuristic to handle multiline imports.
            # It assumes the import ends at the first line without a trailing comma or backslash,
            # or when a closing parenthesis is found. It's not perfect but works for most cases.
            members_str = members_group.split('\n')[0]
            if '(' in members_group and ')' not in members_str:
                members_str = members_group.split(')')[0]

            members_str = members_str.replace('(', '').replace('\\', '').strip()
            
            # Split by comma and clean up each member
            members = [clean_member(m) for m in members_str.split(',') if clean_member(m)]
            for member in members:
                if member == '*':
                    api_usage[module]["*"].append(rel_path)
                elif member:
                    api_usage[module][member].append(rel_path)

    return api_usage

def generate_report(api_usage):
    """
    Generates a markdown report from the collected API usage data.
    """
    report = "### API Usage Report\n\n"
    sorted_modules = sorted(api_usage.keys())

    # A simple filter for Python standard library and known local modules
    # A more robust solution would use a comprehensive list of stdlib modules
    stdlib_guess = ['os', 'sys', 're', 'glob', 'collections', 'logging', 'argparse', 'json', 'math', 'random', 'time', 'pathlib', 'typing', 'abc', 'functools', 'itertools', 'subprocess', 'threading', 'warnings', 'copy', 'inspect', 'shutil', 'tempfile', 'unittest', 'pickle', 'cv2']
    known_local = ['densepose', 'detectron2', 'model', 'utils', 'app', 'inference', 'eval']
    
    for module in sorted_modules:
        top_level_module = module.split('.')[0]
        if top_level_module in stdlib_guess or top_level_module in known_local:
            continue

        report += f"-   **{module}**:\n"
        sorted_members = sorted(api_usage[module].keys())
        for member in sorted_members:
            files = sorted(list(set(api_usage[module][member])))
            files_display = ", ".join(f"`{f}`" for f in files[:3])
            if len(files) > 3:
                files_display += ", ..."
            
            if member == "*module*":
                 report += f"    -   `{module}` (module import): Used in {files_display}\n"
            elif member == "*":
                 report += f"    -   `*` (wildcard import): Used in {files_display}\n"
            else:
                 report += f"    -   `{member}`: Used in {files_display}\n"
        report += "\n"
        
    return report

if __name__ == "__main__":
    project_root = os.getcwd()
    usage_data = analyze_dependencies(project_root)
    markdown_report = generate_report(usage_data)
    
    report_filename = "API_USAGE_REPORT.md"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(markdown_report)
        
    print(f"\nAnalysis complete. Report saved to {report_filename}")
    print("\n--- Report Preview ---")
    print(markdown_report)
