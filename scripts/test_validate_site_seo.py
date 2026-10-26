import tempfile
import unittest
from pathlib import Path

from validate_site_seo import validate


class ValidateSiteSeoTests(unittest.TestCase):
    def test_accepts_canonical_pages_and_internal_redirects(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "site"
            docs = root / "docs"
            (site / "new").mkdir(parents=True)
            (site / "old").mkdir(parents=True)
            (docs / "old").mkdir(parents=True)
            (site / "new" / "index.html").write_text('<link rel="canonical" href="https://docs.trmregistry.com/new/">')
            redirect = '<meta http-equiv="refresh" content="0; url=/new/"><link rel="canonical" href="https://docs.trmregistry.com/new/">'
            (site / "old" / "index.html").write_text(redirect)
            (docs / "old" / "index.html").write_text(redirect)
            self.assertEqual(validate(site, docs, "https://docs.trmregistry.com/"), [])

    def test_rejects_wrong_canonicals_and_missing_redirect_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "site"
            docs = root / "docs"
            (site / "page").mkdir(parents=True)
            (site / "page" / "index.html").write_text('<link rel="canonical" href="https://example.com/wrong/">')
            errors = validate(site, docs, "https://docs.trmregistry.com/")
            self.assertEqual(len(errors), 1)
            self.assertIn("expected", errors[0])


if __name__ == "__main__":
    unittest.main()
