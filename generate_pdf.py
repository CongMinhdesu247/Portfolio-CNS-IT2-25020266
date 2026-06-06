import os
import sys
import subprocess
import shutil

# Files to merge in order
PAGES = [
    "index.html",
    "projects.html",
    "pages/project-1.html",
    "pages/project-2.html",
    "pages/project-3.html",
    "pages/project-4.html",
    "pages/project-5.html",
    "pages/project-6.html",
    "pages/project-7.html",
    "summary.html"
]

OUTPUT_NAME = "DigitalPortfolio_25020266_NguyenCongMinh.pdf"

def in_virtualenv():
    # Detect if we are running inside our temporary virtualenv
    return sys.prefix != sys.base_prefix

def bootstrap():
    print("Setting up virtual environment for PDF merging...")
    venv_dir = os.path.join(os.getcwd(), ".venv_pdf")
    
    # Create virtual environment
    subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    
    # Install pypdf
    pip_path = os.path.join(venv_dir, "bin", "pip")
    print("Installing pypdf in temporary virtual environment...")
    subprocess.run([pip_path, "install", "pypdf"], check=True)
    
    # Re-run script with venv python
    python_path = os.path.join(venv_dir, "bin", "python")
    print("Running PDF generation script inside virtual environment...")
    result = subprocess.run([python_path] + sys.argv)
    
    # Clean up venv
    print("Cleaning up temporary virtual environment...")
    if os.path.exists(venv_dir):
        shutil.rmtree(venv_dir)
    
    sys.exit(result.returncode)

def main():
    workspace = os.getcwd()
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    # Check if Chrome exists
    if not os.path.exists(chrome_path):
        print(f"Error: Chrome not found at '{chrome_path}'")
        print("Please verify your Google Chrome installation path.")
        sys.exit(1)
        
    temp_pdfs = []
    
    print("Generating PDFs for individual pages...")
    for i, page in enumerate(PAGES):
        html_path = os.path.join(workspace, page)
        if not os.path.exists(html_path):
            print(f"Warning: {html_path} does not exist. Skipping.")
            continue
            
        temp_pdf = os.path.join(workspace, f"temp_{i}.pdf")
        temp_pdfs.append(temp_pdf)
        
        print(f"[{i+1}/{len(PAGES)}] Rendering {page} to PDF...")
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={temp_pdf}",
            f"file://{html_path}"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error rendering {page}: {result.stderr}")
            # Clean up and exit
            for f in temp_pdfs:
                if os.path.exists(f):
                    os.remove(f)
            sys.exit(1)
            
    # Merge PDFs
    print("Merging PDFs...")
    try:
        from pypdf import PdfWriter
        merger = PdfWriter()
        for pdf in temp_pdfs:
            if os.path.exists(pdf):
                merger.append(pdf)
            
        output_path = os.path.join(workspace, OUTPUT_NAME)
        merger.write(output_path)
        merger.close()
        print(f"\nSuccess! Successfully created merged PDF: {OUTPUT_NAME}")
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        sys.exit(1)
    finally:
        # Clean up temp PDFs
        print("Cleaning up temporary page PDFs...")
        for f in temp_pdfs:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    if not in_virtualenv():
        bootstrap()
    else:
        main()
