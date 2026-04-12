"""Post-render script to fix sitemap.xml issues:
1. URL-encode spaces in URLs (required by XML/sitemap spec)
2. Replace /index.html with / to match canonical URL
"""
import re
from pathlib import Path
from urllib.parse import quote

SITEMAP = Path(__file__).parent / "docs" / "sitemap.xml"


def fix_sitemap():
    if not SITEMAP.exists():
        print("sitemap.xml not found, skipping fix")
        return

    content = SITEMAP.read_text(encoding="utf-8")

    def encode_loc(match):
        url = match.group(1)
        # Split into base and path
        prefix = "https://vectoringai.com/"
        if url.startswith(prefix):
            path = url[len(prefix):]
            # Replace index.html at root with empty (becomes just /)
            if path == "index.html":
                path = ""
            # URL-encode spaces and other special chars in path segments
            parts = path.split("/")
            encoded_parts = [quote(part, safe="") for part in parts]
            encoded_path = "/".join(encoded_parts)
            return f"<loc>{prefix}{encoded_path}</loc>"
        return match.group(0)

    fixed = re.sub(r"<loc>(.*?)</loc>", encode_loc, content)

    SITEMAP.write_text(fixed, encoding="utf-8")
    print("sitemap.xml fixed: URL-encoded spaces and normalized index.html")


if __name__ == "__main__":
    fix_sitemap()
