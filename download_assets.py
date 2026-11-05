#!/usr/bin/env python3
"""Fetch required Figma media from publicly accessible Healthify prototype.
Requires an internet connection. All media SHA-1 hashes are checked.
"""
from pathlib import Path
import argparse, hashlib, json, sys, urllib.request

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'assets-manifest.json').read_text(encoding='utf-8'))
base_url = 'https://healthify-demo.vercel.app/'
parser = argparse.ArgumentParser()
parser.add_argument('--verify-only',action='store_true',help='Check local assets without downloading')
args = parser.parse_args()
errors=[]
for name,record in manifest.items():
    target=root/name
    if target.exists():
        data=target.read_bytes()
        if hashlib.sha1(data).hexdigest()==record['sha1'] and len(data)==record['bytes']:
            print('OK',name)
            continue
    if args.verify_only:
        print('MISSING/INVALID',name)
        errors.append(name)
        continue
    url=base_url+name
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 HealthifyDeveloperHandoff/1.0'})
        with urllib.request.urlopen(request,timeout=30) as response:
            data=response.read()
        sha=hashlib.sha1(data).hexdigest()
        if sha!=record['sha1'] or len(data)!=record['bytes']:
            raise ValueError(f'Asset checksum or length differs from expected build: {name} ({len(data)} bytes, sha={sha})')
        target.write_bytes(data)
        print('DOWNLOADED',name)
    except Exception as exc:
        print('ERROR',name,str(exc),file=sys.stderr)
        errors.append(name)
if errors:
    print(f'FAILED: {len(errors)} assets. Check network access and retry.',file=sys.stderr)
    raise SystemExit(1)
print('All 10 Figma assets verified.')
