// Curriculum Data Module - Outcomes version (drop-in replacement)
const curriculumData = {
  title: "What You’ll Walk Away With — Your Investor Playbook",

  parts: [
    {
      id: 1,
      title: "PART 1 — Build an Unshakable Foundation",
      modules: [
        { type: "outcome", title: "Explain what truly drives business value and investor returns in plain English." },
        { type: "outcome", title: "Spot where most investors go wrong — and avoid those traps before they cost you." },
        { type: "outcome", title: "Identify your circle of competence and invest where you actually have an edge." },
        { type: "outcome", title: "Operate with a calm, rules-based mindset instead of headlines, FOMO, or fear." },
        { type: "outcome", title: "Read market psychology and herd behavior without getting pulled into it." }
      ]
    },

    {
      id: 2,
      title: "PART 2 — Think Like a Professional Analyst",
      modules: [
        { type: "outcome", title: "Differentiate business models (e.g., banks vs. software, Netflix vs. legacy media) and value them appropriately." },
        { type: "outcome", title: "Recognize optionality and asymmetric payoff structures before the crowd sees them." },
        { type: "outcome", title: "Run a clean sourcing process to find ideas — and filter out value traps quickly." },
        { type: "outcome", title: "Evaluate management, governance, and incentives as first-class drivers of outcomes." },
        { type: "outcome", title: "Map ranges of outcomes instead of false precision — and anchor to base rates." },
        { type: "outcome", title: "Understand technological disruption and product/industry life cycles to time your exposure." }
      ]
    },

    {
      id: 3,
      title: "PART 3 — Become a Master Investor",
      modules: [
        { type: "outcome", title: "Apply simple, high-efficiency frameworks ('cheat codes' & convex heuristics) to make faster, better decisions." },
        { type: "outcome", title: "Compare real company strategies (Domino’s vs. Nvidia, Starbucks vs. Google) to sharpen your own playbook." },
        { type: "outcome", title: "Use macro context pragmatically — ride big trends without turning into a tourist." },
        { type: "outcome", title: "Synthesize psychology, business insight, and data into a coherent, repeatable edge." }
      ]
    },

    {
      id: 4,
      title: "PART 4 — Manage Risk & Build a Durable Portfolio",
      modules: [
        { type: "outcome", title: "Construct a portfolio that survives disruption, de-globalization, and model risk — not just bull markets." },
        { type: "outcome", title: "Position sizing and adds/trims that reflect probabilities, not emotions." },
        { type: "outcome", title: "Recognize reflexivity, boom/bust dynamics, and micro-bubbles — and act before they act on you." },
        { type: "outcome", title: "Leave with a personal operating system: risk rules, decision checklists, and a way to audit your own thinking." }
      ]
    }
  ]
};

// Function to generate curriculum HTML (unchanged structure)
function generateCurriculumHTML() {
  let html = `
    <section class="curriculum" id="curriculum">
      <div class="container">
        <div class="curriculum-content">
          <h2>${curriculumData.title}</h2>
  `;

  curriculumData.parts.forEach(part => {
    html += `
          <div class="curriculum-part">
            <div class="part-header">
              <h3 class="part-title">${part.title}</h3>
            </div>
            <div class="modules-list">
    `;

    part.modules.forEach(module => {
      let moduleClass = "module-item";
      if (module.type === "case-study") moduleClass += " case-study";
      else if (module.type === "live-workshop") moduleClass += " live-workshop";
      // 'outcome' falls back to default styling so your CSS works without changes

      html += `
              <div class="${moduleClass}">
                <h4 class="module-title">${module.title}</h4>
              </div>
      `;
    });

    html += `
            </div>
          </div>
    `;
  });

  html += `
        </div>
      </div>
    </section>
  `;

  return html;
}

// (Optional) Keep live workshop CSS export intact; outcomes don't use it but harmless to leave.
const liveWorkshopCSS = `
/* ===== LIVE WORKSHOP STYLING ===== */
.live-workshop {
    background: #2C3E4A !important;
    border: 2px solid #FF8C42 !important;
    position: relative;
}
.live-workshop::before {
    content: "LIVE WORKSHOP";
    position: absolute;
    top: -10px;
    left: 20px;
    background: #FF8C42;
    color: #fff;
    padding: 5px 15px;
    border-radius: 5px;
    font-size: 0.8rem;
    font-weight: bold;
    letter-spacing: 0.5px;
}
.live-workshop .module-title {
    color: #fff !important;
}
`;

// Export for use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { curriculumData, generateCurriculumHTML, liveWorkshopCSS };
}
