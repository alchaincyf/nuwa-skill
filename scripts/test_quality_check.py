"""Regression tests for source section extraction.

Run with: python3 -m unittest discover -s scripts -p 'test_*.py' -v
"""

import unittest

from quality_check import check_primary_sources


class PrimarySourcesTests(unittest.TestCase):
    def test_nested_source_headings_remain_in_section(self):
        content = """# Example
## Overview
Notes mentioning 来源 in the body.
## 调研来源
### 一手来源
- 原始访谈 A
- 原始访谈 B
- 原始访谈 C
### 二手来源
- 评论 D
## Other
primary primary primary
"""
        passed, detail = check_primary_sources(content)
        self.assertTrue(passed)
        self.assertIn("4/6 (67%)", detail)

    def test_following_section_is_excluded(self):
        content = "## Sources\n- primary\n- secondary\n## Notes\nprimary primary primary\n"
        passed, detail = check_primary_sources(content)
        self.assertFalse(passed)
        self.assertIn("1/2 (50%)", detail)

    def test_subheading_alone_is_not_a_source_section(self):
        passed, detail = check_primary_sources("## Overview\n### Sources\n- secondary\n")
        self.assertTrue(passed)
        self.assertEqual(detail, "未找到来源section（跳过检查）")

    def test_body_mention_is_not_a_source_heading(self):
        content = "## Overview\nThe 来源 section is not present.\n- secondary\n"
        passed, detail = check_primary_sources(content)
        self.assertTrue(passed)
        self.assertEqual(detail, "未找到来源section（跳过检查）")

    def test_supported_headings_and_line_endings(self):
        for heading in ("## Sources", "## References", "## 附录：调研来源", "## sources"):
            for newline in ("\n", "\r\n"):
                with self.subTest(heading=heading, newline=repr(newline)):
                    content = newline.join((heading, "- primary", "- primary", "- secondary"))
                    passed, detail = check_primary_sources(content)
                    self.assertTrue(passed)
                    self.assertIn("2/3 (67%)", detail)

    def test_empty_section_does_not_consume_following_section(self):
        passed, detail = check_primary_sources("## Sources\n## Notes\n- secondary\n")
        self.assertTrue(passed)
        self.assertEqual(detail, "未标记来源类型（跳过检查）")

    def test_low_primary_ratio_still_fails(self):
        content = "## Sources\n- primary\n- secondary\n- secondary\n- secondary\n"
        passed, detail = check_primary_sources(content)
        self.assertFalse(passed)
        self.assertIn("1/4 (25%)", detail)

    def test_unmarked_sources_are_skipped(self):
        passed, detail = check_primary_sources("## Sources\n- https://example.com\n")
        self.assertTrue(passed)
        self.assertEqual(detail, "未标记来源类型（跳过检查）")

    def test_heading_at_end_of_file(self):
        passed, detail = check_primary_sources("## Sources")
        self.assertTrue(passed)
        self.assertEqual(detail, "未标记来源类型（跳过检查）")


if __name__ == "__main__":
    unittest.main()
