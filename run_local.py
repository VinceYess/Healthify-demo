#!/usr/bin/env python3
"""Fetch the original Figma files and serve the Healthify prototype locally."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import os,subprocess,sys
root=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(root/'download_assets.py')],cwd=root,check=True)
os.chdir(root)
print('Open http://localhost:8000/ (Ctrl+C to stop)',flush=True)
ThreadingHTTPServer(('127.0.0.1',8000),SimpleHTTPRequestHandler).serve_forever()
