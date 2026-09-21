"""Full site build: generate all pages + ads.txt + robots.txt + IndexNow key file + sitemap.xml."""
import datetime
import hashlib
import json
import os

import generate
from static_pages import ADSENSE_CLIENT, BASE_URL, page_url

OUTPUT_DIR = generate.OUTPUT_DIR

# IndexNow key (Bing and the other participating engines). docs/<key>.txt has to be live on the
# site for indexnow.py pings to be accepted.
INDEXNOW_KEY = "2924969a0b87717fbfd6bcfa77d78698"

# Records when each page's content actually changed (kept outside docs/, so it isn't published).
LASTMOD_MANIFEST = "lastmod.json"


def build_ads_txt():
    pub_id = ADSENSE_CLIENT.replace("ca-pub-", "pub-")
    content = f"google.com, {pub_id}, DIRECT, f08c47fec0942fa0\n"
    with open(os.path.join(OUTPUT_DIR, "ads.txt"), "w", encoding="utf-8") as f:
        f.write(content)
    print("ads.txt written")


def build_robots_txt():
    content = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n"
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(content)
    print("robots.txt written")


def build_indexnow_key():
    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)


def build_sitemap(pages):
    # lastmod only moves to today for pages whose content hash changed. Stamping every page with
    # today's date on every build teaches search engines to ignore lastmod entirely.
    try:
        with open(LASTMOD_MANIFEST, encoding="utf-8") as f:
            manifest = json.load(f)
    except FileNotFoundError:
        manifest = {}
    today = datetime.date.today().isoformat()

    new_manifest = {}
    entries = []
    for fname in sorted(pages, key=lambda f: (f != "index.html", f)):
        with open(os.path.join(OUTPUT_DIR, fname), "rb") as f:
            digest = hashlib.sha256(f.read().replace(b"\r\n", b"\n")).hexdigest()
        prev = manifest.get(fname)
        lastmod = prev["lastmod"] if prev and prev["sha256"] == digest else today
        new_manifest[fname] = {"sha256": digest, "lastmod": lastmod}
        entries.append(f"  <url><loc>{page_url(fname)}</loc><lastmod>{lastmod}</lastmod></url>")

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    with open(LASTMOD_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(new_manifest, f, indent=1, sort_keys=True)
    print(f"sitemap.xml written ({len(entries)} URLs)")


def main():
    pages = generate.main()
    build_ads_txt()
    build_robots_txt()
    build_indexnow_key()
    build_sitemap(pages)


if __name__ == "__main__":
    main()
