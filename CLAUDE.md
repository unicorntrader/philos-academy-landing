# Philo's Academy landing page

Static HTML site (no build step), deployed by Vercel from `main` to philomastery.com.
Push straight to `main` — no pull requests. Show visual changes as screenshots in chat
before shipping; don't send preview links.

## Colour conventions

Tokens live in `:root` in `index.html`: `--cream`, `--navy`, `--ink`, `--brand`, `--line`.

Every section gets exactly one background class. Containers follow from it — never
hand-pick a container colour.

| Section class | Big container (`.section-shell`) | Small cards (module cards, rows, tabs) | Text |
|---|---|---|---|
| `.bg-cream` | white | white + `--line` border | ink |
| `.bg-white` | cream | white + `--line` border | ink |
| `.bg-navy`  | none — content sits on navy | white + `--line` border, dark text | cream |

Rules:
- Light sections alternate cream / white down the page.
- Navy is the accent surface: at most ~2 per page, never two in a row. Currently the
  email signup band and "Results, Applied".
- Orange (`--brand`) is for buttons, eyebrows and highlights. The only orange section is
  the closing CTA.
- No dark container on a dark section, no cream container on a cream section.
