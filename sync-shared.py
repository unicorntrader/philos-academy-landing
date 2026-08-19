#!/usr/bin/env python3
"""
Keeps the header (topnav + mobile panel) and footer blocks byte-identical
across index.html, modules.html, and faq.html.

This is NOT part of the deploy pipeline -- the site is served as plain
committed HTML, unchanged. Run this locally after editing the header/footer
template below, then commit the regenerated files like any other edit. It
exists to stop the "fixed 2 of 3 pages" class of bug (nav CSS or links
drifting out of sync between pages), copied from ct3000-landing's own
sync-shared.py.

Legal pages (privacy.html, terms.html, disclaimer.html) use a deliberately
separate, minimal header -- not the full marketing nav -- and are not
touched by this script.

Usage:
    python3 sync-shared.py            # rewrite header+footer in all pages
    python3 sync-shared.py --check    # exit 1 if any page would change
"""
import re
import sys

LOGO_IMG = '<img src="/philo-owl-mark.png" alt="" width="240" height="255">'


def cls(active):
    return ' class="current"' if active else ''


def nav_links(page):
    """page: 'home' | 'inside-the-course' | 'faq'"""
    is_home = page == 'home'
    course_href = '#outcomes' if is_home else '/index.html#outcomes'
    inside_href = '#inside-the-course' if is_home else '/modules.html'
    fit_href = '#audience-fit-cards' if is_home else '/index.html#audience-fit-cards'
    inside_c = cls(page == 'inside-the-course')
    faq_c = cls(page == 'faq')
    return (
        f'<a href="{course_href}">The Course</a>\n'
        f'      <a href="{inside_href}"{inside_c}>Inside The Course</a>\n'
        f'      <a href="{fit_href}">Is This For You</a>\n'
        f'      <a href="/faq.html"{faq_c}>FAQ</a>'
    )


def build_header(page):
    is_home = page == 'home'
    logo_href = '#top' if is_home else '/index.html#top'
    links = nav_links(page)
    mobile_links = links.replace('\n      ', '\n    ')
    return f'''<header class="topnav">
    <a href="{logo_href}" class="topnav-logo">{LOGO_IMG}Philo's Academy</a>
    <nav class="topnav-links">
      {links}
      <button type="button" class="topnav-burger" id="navBurger" aria-label="Toggle menu" aria-expanded="false" aria-controls="navMobilePanel">
        <span></span><span></span><span></span>
      </button>
      <a href="https://whop.com/checkout/plan_G0hXojwo3WzJQ" class="topnav-cta">Start Learning</a>
    </nav>
  </header>
  <div class="topnav-mobile-panel" id="navMobilePanel">
    {mobile_links}
    <a href="https://whop.com/checkout/plan_G0hXojwo3WzJQ" class="topnav-cta">Start Learning</a>
  </div>'''


def build_footer(page):
    is_home = page == 'home'
    course_href = '#outcomes' if is_home else '/index.html#outcomes'
    inside_href = '#inside-the-course' if is_home else '/modules.html'
    fit_href = '#audience-fit-cards' if is_home else '/index.html#audience-fit-cards'
    return f'''<footer>
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="mark">{LOGO_IMG}Philo's Academy</div>
        <p>Learn Investing. Better.</p>
      </div>
      <div class="footer-col">
        <h5>Explore</h5>
        <a href="{course_href}">The Course</a>
        <a href="{inside_href}">Inside The Course</a>
        <a href="{fit_href}">Is This For You</a>
        <a href="/faq.html">FAQ</a>
      </div>
      <div class="footer-col">
        <h5>Connect</h5>
        <a href="https://x.com/philoinvestor" target="_blank" rel="noopener">@philoinvestor</a>
        <a href="https://youtube.com/@philos_academy" target="_blank" rel="noopener">YouTube</a>
        <a href="https://philoinvestor.com" target="_blank" rel="noopener">Philoinvestor</a>
      </div>
      <div class="footer-col">
        <h5>Legal</h5>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms of Service</a>
        <a href="/disclaimer.html">Disclaimer</a>
      </div>
    </div>
    <div class="footer-legal">
      &copy; 2026 Philo's Academy. Learn Investing. Better.
    </div>
  </footer>'''


# filename -> page type
PAGES = {
    'index.html':   'home',
    'modules.html': 'inside-the-course',
    'faq.html':     'faq',
}

HEADER_RE = re.compile(
    r'<header class="topnav">.*?</header>\s*<div class="topnav-mobile-panel"[^>]*>.*?</div>',
    re.DOTALL,
)
FOOTER_RE = re.compile(r'<footer>.*?</footer>', re.DOTALL)


def main():
    check_only = '--check' in sys.argv
    changed = []
    for fname, page in PAGES.items():
        header = build_header(page)
        footer = build_footer(page)

        with open(fname, encoding='utf-8') as f:
            content = f.read()

        new_content = HEADER_RE.sub(lambda m: header, content, count=1)
        new_content = FOOTER_RE.sub(lambda m: footer, new_content, count=1)

        if new_content != content:
            changed.append(fname)
            if not check_only:
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    if check_only:
        if changed:
            print('Out of sync:', ', '.join(changed))
            sys.exit(1)
        print('All pages in sync.')
    else:
        print(f'Synced. Changed: {changed if changed else "none"}')


if __name__ == '__main__':
    main()
