// KCM Collapse Simulator Logic v0.1
// Author: Saurabh Misra (Karnav)

const KCM_UI = (() => {
  function $(id) {
    return document.getElementById(id);
  }

  function updateValue(spanId, value) {
    const el = $(spanId);
    if (el) el.textContent = value;
  }

  function computeCollapse() {
    const signalText = $("signalInput").value.trim();

    const meaningClarity = Number($("meaningClarity").value || 0);
    const routeOptions = Number($("routeOptions").value || 0);
    const trustScore = Number($("trustScore").value || 0);
    const timePressure = Number($("timePressure").value || 0);
    const instabilityLevel = Number($("instabilityLevel").value || 0);

    // Basic stability model inspired by Collapse-Math-Foundation:
    // Higher clarity, trust, and lower instability/time-pressure → better stability.
    const stabilityScore = Math.round(
      (meaningClarity + trustScore + (100 - instabilityLevel) + (100 - timePressure)) / 4
    );

    // Interpret routeOptions as behaviour-space width
    let branchComplexity;
    if (routeOptions < 30) branchComplexity = "Low (few paths)";
    else if (routeOptions < 70) branchComplexity = "Medium (balanced options)";
    else branchComplexity = "High (many competing paths)";

    let collapseClass;
    let collapseLabel;
    if (stabilityScore >= 70) {
      collapseClass = "Stable Centered Collapse";
      collapseLabel = "HIGH STABILITY (center-locked)";
    } else if (stabilityScore >= 40) {
      collapseClass = "Semi-Stable Collapse";
      collapseLabel = "MID STABILITY (needs refinement)";
    } else {
      collapseClass = "Unstable / Premature Collapse";
      collapseLabel = "LOW STABILITY (re-collapse likely)";
    }

    // Simple energy-style metric from spec: E(x) = D(x) + C(x)
    const D = Math.round(Math.abs(50 - stabilityScore)); // pseudo distance from center
    const C = Math.round(instabilityLevel / 2);          // contradiction proxy
    const E = D + C;

    const explanation = [];

    explanation.push(`▶ 1. INPUT (Wave-State)\n${signalText || "[No explicit text provided]"}`);
    explanation.push("");
    explanation.push("▶ 2. KRP ROOT SNAPSHOT");
    explanation.push(`   • MeaningRoot (MR) – Clarity: ${meaningClarity}/100`);
    explanation.push(`   • RouteRoot (RR) – Options: ${routeOptions}/100 → ${branchComplexity}`);
    explanation.push(`   • TrustRoot (TR) – Reliability: ${trustScore}/100`);
    explanation.push(`   • TimeRoot (TmR) – Time Pressure: ${timePressure}/100`);
    explanation.push(`   • Instability / Contradiction: ${instabilityLevel}/100`);
    explanation.push("");
    explanation.push("▶ 3. COLLAPSE METRICS (Simplified KCM Math)");
    explanation.push(`   • StabilityScore ≈ ${stabilityScore}/100`);
    explanation.push(`   • Distance from Center D(x) ≈ ${D}`);
    explanation.push(`   • Contradiction Magnitude C(x) ≈ ${C}`);
    explanation.push(`   • Energy E(x) = D(x) + C(x) ≈ ${E}`);
    explanation.push("");
    explanation.push("▶ 4. C-STATE CLASSIFICATION");
    explanation.push(`   • Collapse Type: ${collapseClass}`);
    explanation.push(`   • Stability Label: ${collapseLabel}`);
    explanation.push("");

    explanation.push("▶ 5. KCM INTERPRETATION (MR → RR → TR → TmR → C)");
    if (stabilityScore >= 70) {
      explanation.push(
        "   The system is close to its center. KRP roots are sufficiently aligned. " +
        "This is a good final decision-state under the current configuration."
      );
    } else if (stabilityScore >= 40) {
      explanation.push(
        "   The system has partially aligned roots. A decision is possible, but KCM suggests " +
        "refining either meaning clarity (MR) or structural trust (TR) before treating this as final."
      );
    } else {
      explanation.push(
        "   KCM flags this as an unstable collapse: contradiction and distance from center are high. " +
        "Reframe the situation (MR) and reduce instability before committing."
      );
    }

    explanation.push("");
    explanation.push("▶ 6. SUGGESTED TWEAKS (Based on KCM):");
    if (meaningClarity < 50) {
      explanation.push("   • Increase MeaningRoot (MR): Clarify the real question or intent.");
    }
    if (trustScore < 50) {
      explanation.push("   • Strengthen TrustRoot (TR): Remove options that violate core constraints.");
    }
    if (instabilityLevel > 60) {
      explanation.push("   • Reduce Instability: Remove contradictions, conflicting goals, or noise.");
    }
    if (timePressure > 70) {
      explanation.push("   • Reduce Time Pressure (TmR): Allow slightly more time for a better collapse.");
    }
    if (
      meaningClarity >= 50 &&
      trustScore >= 50 &&
      instabilityLevel <= 60 &&
      timePressure <= 70
    ) {
      explanation.push("   • Current configuration is acceptable for a real-world collapse decision.");
    }

    return explanation.join("\n");
  }

  function runSimulation() {
    const btn = $("simulateBtn");
    if (btn) btn.disabled = true;

    const output = computeCollapse();
    const target = $("collapseSummary");
    if (target) target.textContent = output;

    if (btn) {
      setTimeout(() => {
        btn.disabled = false;
      }, 300);
    }
  }

  return {
    updateValue,
    runSimulation
  };
})();
