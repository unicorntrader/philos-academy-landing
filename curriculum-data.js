// Curriculum data structure - simplified outcomes-only version
const curriculumData = {
  title: "Who You'll Become",
  parts: [
    {
      id: 1,
      title: "PART 1 — Build an Unshakable Foundation",
      outcomes: [
        "Understand what really drives business value and investor returns — in plain English.",
        "Spot where most investors go wrong and avoid those traps before they cost you.",
        "Invest with confidence in areas where you actually have an edge."
      ]
    },
    {
      id: 2,
      title: "PART 2 — Think Like a Professional Analyst",
      outcomes: [
        "Differentiate business models (banks vs. software, Netflix vs. legacy media) and value them appropriately.",
        "Recognize optionality, disruption, and innovation before the market does.",
        "Source ideas and filter out value traps with a systematic process."
      ]
    },
    {
      id: 3,
      title: "PART 3 — Develop Your Strategy & Edge",
      outcomes: [
        "Distinguish simplicity from complexity and focus on high-efficiency frameworks.",
        "Integrate macro trends, business models, and conviction into your own strategy.",
        "Start thinking and acting like a master investor — systematic, calm, decisive."
      ]
    },
    {
      id: 4,
      title: "PART 4 — Achieve Resilience & Portfolio Mastery",
      outcomes: [
        "Build and manage a portfolio that survives disruption and uncertainty.",
        "Master risk management frameworks — from boom/bust cycles to reflexivity.",
        "Become your own edge: apply judgment, adaptability, and discipline in every market."
      ]
    }
  ]
};

// Function to generate simplified curriculum HTML
function generateCurriculumHTML() {
  let html = `
    <section class="outcomes" style="padding:80px 0; background:#fff;">
      <div class="container">
        <h2 style="text-align:center; font-size:2.2rem; margin-bottom:50px; color:#2C3E4A;">
          ${curriculumData.title}
        </h2>
  `;

  curriculumData.parts.forEach(part => {
    html += `
        <div style="margin-bottom:40px;">
          <h3 style="color:#FF8C42; font-size:1.5rem; margin-bottom:12px;">
            ${part.title}
          </h3>
          <ul style="list-style:disc; margin-left:20px; color:#2C3E4A; line-height:1.6;">
    `;
    
    part.outcomes.forEach(outcome => {
      html += `            <li>${outcome}</li>`;
    });
    
    html += `
          </ul>
        </div>
    `;
  });

  html += `
      </div>
    </section>
  `;

  return html;
}

// Export for use in other files (if using modules)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { curriculumData, generateCurriculumHTML };
}
