// Curriculum Data Module - All course content organized
const curriculumData = {
  title: "The Journey: 28 Modules & 8 Case Studies",
  
  parts: [
    {
      id: 1,
      title: "PART 1 — Foundational Concepts & Value Investing",
      modules: [
        { type: "module", title: "Introduction to Investing" },
        { type: "module", title: "Value Investing 101" },
        { type: "module", title: "Building Blocks to Value" },
        { type: "module", title: "What Drives Value?" },
        { type: "live-workshop", title: "Live Workshop" }, // LIVE WORKSHOP ADDED HERE
        { type: "module", title: "Next-Level Thinking" },
        { type: "module", title: "Where Investors Go Wrong" },
        { type: "module", title: "Investing Where You Have an Edge" },
        { type: "module", title: "Psychology of Investing" },
        { type: "case-study", title: "Major Investing Mistakes" },
        { type: "module", title: "Psychology of Markets & Herd Behavior" }
      ]
    },
    
    {
      id: 2,
      title: "PART 2 — Advanced Investment Concepts",
      modules: [
        { type: "module", title: "Understanding Market Dimensions: Price, Value & Liquidity" },
        { type: "module", title: "Differentiating Business Models" },
        { type: "case-study", title: "Netflix vs Legacy Media" },
        { type: "case-study", title: "Banking vs Software" },
        { type: "module", title: "Unlocking Optionality in Investing" },
        { type: "case-study", title: "Duolingo & Moderna" },
        { type: "live-workshop", title: "Live Workshop" }, // LIVE WORKSHOP ADDED HERE
        { type: "module", title: "Research & Idea Sourcing" },
        { type: "module", title: "Avoiding Bad Companies & Value Traps" },
        { type: "case-study", title: "Range of Outcomes" },
        { type: "module", title: "Management, Governance & Ethics" },
        { type: "case-study", title: "Teledyne vs Snapchat" },
        { type: "module", title: "Technological Disruption & Innovation" },
        { type: "module", title: "Not All Business Is Made the Same" },
        { type: "module", title: "Life Cycles" }
      ]
    },
    
    {
      id: 3,
      title: "PART 3 — Mastery & Strategy",
      modules: [
        { type: "module", title: "Simplicity vs Complexity" },
        { type: "case-study", title: "Domino's vs Nvidia" },
        { type: "live-workshop", title: "Live Workshop" }, // LIVE WORKSHOP ADDED HERE
        { type: "case-study", title: "Starbucks vs Google" },
        { type: "module", title: "Becoming a Master Investor" },
        { type: "module", title: "High Efficiency Frameworks: Cheat Codes & Convex Heuristics" },
        { type: "module", title: "Macro Investing: Playing the Big Trends" },
        { type: "module", title: "Using Edges to Source Opportunities" }
      ]
    },
    
    {
      id: 4,
      title: "PART 4 — Managing Risk & Portfolio Management",
      modules: [
        { type: "module", title: "Surviving Market Shifts: Disruption, De-Globalization & Business Model Risks" },
        { type: "module", title: "Portfolio Management & Construction" },
        { type: "live-workshop", title: "Live Workshop" }, // LIVE WORKSHOP ADDED HERE
        { type: "module", title: "Thriving in Uncertainty: Risk Management & Decision Making" },
        { type: "module", title: "Reflexivity, Boom/Bust Cycles & Micro-Bubbles" },
        { type: "module", title: "You Are the Edge (and Other Intangible Angles)" }
      ]
    }
  ]
};

// Function to generate curriculum HTML
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
      if (module.type === "case-study") {
        moduleClass += " case-study";
      } else if (module.type === "live-workshop") {
        moduleClass += " live-workshop";
      }
      
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

// CSS for Live Workshop styling
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