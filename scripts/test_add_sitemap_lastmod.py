import subprocess
import tempfile
import unittest
from pathlib import Path

from add_sitemap_lastmod import enrich_sitemap, source_for_location


class SitemapLastmodTests(unittest.TestCase):
    def test_maps_public_urls_to_markdown_sources(self):
        docs = Path("docs")
        self.assertEqual(source_for_location("https://docs.trmregistry.com/", docs), docs / "index.md")
        self.assertEqual(source_for_location("https://docs.trmregistry.com/guide/quickstart/", docs), docs / "guide/quickstart.md")

    def test_uses_the_last_commit_date_for_each_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text("Home")
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
            subprocess.run(["git", "add", "docs/index.md"], cwd=root, check=True)
            environment = {"GIT_AUTHOR_DATE": "2024-02-03T12:00:00Z", "GIT_COMMITTER_DATE": "2024-02-03T12:00:00Z"}
            subprocess.run(["git", "commit", "-qm", "docs"], cwd=root, check=True, env={**__import__("os").environ, **environment})
            xml = '<urlset><url><loc>https://docs.trmregistry.com/</loc></url></urlset>'
            enriched = enrich_sitemap(xml, docs, root)
            self.assertIn("<lastmod>2024-02-03</lastmod>", enriched)

    def test_rejects_sitemap_urls_without_a_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            xml = '<urlset><url><loc>https://docs.trmregistry.com/missing/</loc></url></urlset>'
            with self.assertRaisesRegex(RuntimeError, "No documentation source"):
                enrich_sitemap(xml, root / "docs", root)


if __name__ == "__main__":
    unittest.main()
