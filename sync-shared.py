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


# The nav and footer *CSS* (not just the markup above) also has to stay
# identical across pages -- font sizes, hover treatment, colors. It lives
# between /* SYNC:NAV:START */.../* SYNC:NAV:END */ and the FOOTER
# equivalent in each page's <style> block. Canonical text below, copied
# from index.html; edit it here, not in the individual pages.
NAV_CSS = '''    /* Fixed nav */
    .topnav{
      position:fixed; top:0; left:0; right:0; z-index:200;
      display:flex; align-items:center; justify-content:space-between; gap:16px;
      padding:14px clamp(22px,6vw,42px);
      background:rgba(255,248,231,.92);
      backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px);
      border-bottom:1px solid rgba(44,62,74,.07);
    }
    .topnav-logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:1rem;letter-spacing:-.01em;color:var(--ink);text-decoration:none;white-space:nowrap}
    .topnav-logo img{height:30px;width:auto;display:block}
    .topnav-links{display:flex;align-items:center;gap:clamp(16px,3vw,30px)}
    .topnav-links a{font-weight:600;font-size:15px;letter-spacing:0;color:var(--ink);text-decoration:none}
    .topnav-links a:hover{color:var(--brand)}
    .topnav-links a.current, .topnav-mobile-panel a.current{color:var(--brand)}
    .topnav-links a.topnav-cta{background:var(--brand);color:#fff;padding:10px 20px;border-radius:999px;font-weight:700;white-space:nowrap;transition:background .6s ease,color .6s ease,box-shadow .6s ease}
    .topnav-links a.topnav-cta:hover{background:#fff;color:var(--brand);box-shadow:inset 0 0 0 2px var(--brand)}
    body{padding-top:66px}

    .topnav-burger{display:none;flex-direction:column;justify-content:center;gap:5px;width:26px;height:20px;background:none;border:none;cursor:pointer;padding:0;flex-shrink:0}
    /* Whole-pixel height/translate (not 2.6px/7.6px) plus backface-visibility:hidden --
       subpixel values on a rotating transform inside a blurred (backdrop-filter) parent
       is a known WebKit ghosting trigger: the pre-transform line stays faintly visible
       through the animation instead of cleanly resolving into the X. */
    .topnav-burger span{display:block;height:3px;background:var(--ink);border-radius:2px;transition:transform .2s ease,opacity .2s ease;backface-visibility:hidden;-webkit-backface-visibility:hidden}
    .topnav-burger.open span:nth-child(1){transform:translateY(8px) rotate(45deg)}
    .topnav-burger.open span:nth-child(2){opacity:0}
    .topnav-burger.open span:nth-child(3){transform:translateY(-8px) rotate(-45deg)}

    .topnav-mobile-panel{
      position:fixed; top:66px; left:0; right:0; z-index:199;
      background:rgba(255,255,255,.98); backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px);
      display:flex; flex-direction:column;
      max-height:0; overflow:hidden;
      transition:max-height .3s ease;
    }
    /* border only when open -- max-height:0 collapses the content but a border-bottom
       still paints at that collapsed edge regardless, showing as a faint stray line
       sitting just under the header even while this panel is "closed" */
    .topnav-mobile-panel.open{max-height:400px; border-bottom:1px solid rgba(44,62,74,.08)}
    .topnav-mobile-panel a{padding:13px 22px;font-weight:600;color:var(--ink);text-decoration:none;font-size:1rem;border-top:1px solid rgba(44,62,74,.06)}
    .topnav-mobile-panel a:first-child{border-top:none}
    .topnav-mobile-panel a:hover{color:var(--brand)}
    .topnav-mobile-panel a.topnav-cta{
      background:var(--brand);color:#fff;text-align:center;border-radius:999px;font-weight:700;
      margin:10px 22px 16px;border-top:none;padding:13px 20px;
      transition:background .6s ease,color .6s ease,box-shadow .6s ease;
    }
    .topnav-mobile-panel a.topnav-cta:hover{background:#fff;color:var(--brand);box-shadow:inset 0 0 0 2px var(--brand)}

    @media (max-width:820px){
      .topnav-links a{display:none}
      .topnav-burger{display:flex}
    }
    @media (min-width:821px){
      .topnav-mobile-panel{display:none}
    }'''

FOOTER_CSS = '''    footer{background:var(--cream);padding:clamp(52px,7vw,80px) 0 clamp(28px,4vw,40px);border-top:2px solid var(--brand)}
    .footer-inner{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:clamp(24px,4vw,48px);max-width:1080px;margin:0 auto;padding:0 clamp(20px,5vw,48px)}
    .footer-brand .mark{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.3rem;color:var(--ink);margin-bottom:10px}
    .footer-brand .mark img{height:36px;width:auto;display:block}
    .footer-brand p{color:#6b6156;font-size:.92rem;line-height:1.5;max-width:32ch;margin:0}
    .footer-col h5{font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--brand);margin:0 0 14px}
    .footer-col a{display:block;color:#4a4640;font-size:15px;text-decoration:none;margin-bottom:10px}
    .footer-col a:hover{color:var(--brand)}
    .footer-legal{max-width:1080px;margin:clamp(40px,5vw,60px) auto 0;padding:24px clamp(20px,5vw,48px) 0;border-top:1px solid rgba(44,62,74,.12);color:#9a9186;font-size:13px;text-align:center}
    @media (max-width:700px){.footer-inner{grid-template-columns:1fr 1fr}}'''


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
NAV_CSS_RE = re.compile(r'(?<=SYNC:NAV:START -- kept in sync across pages by sync-shared.py, edit there \*/\n).*?(?=\n {4}/\* SYNC:NAV:END \*/)', re.DOTALL)
FOOTER_CSS_RE = re.compile(r'(?<=SYNC:FOOTER:START -- kept in sync across pages by sync-shared.py, edit there \*/\n).*?(?=\n {4}/\* SYNC:FOOTER:END \*/)', re.DOTALL)


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
        new_content = NAV_CSS_RE.sub(lambda m: NAV_CSS, new_content, count=1)
        new_content = FOOTER_CSS_RE.sub(lambda m: FOOTER_CSS, new_content, count=1)

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
