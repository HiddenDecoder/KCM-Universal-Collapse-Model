# State Resolver Module (KCM Engine)
# Author: Saurabh Misra (Karnav)
#
# This module handles the actual C-State computation:
#   - stability score
#   - distance from center D(x)
#   - contradiction magnitude C(x)
#   - collapse energy E(x) = D(x) + C(x)
#   - final collapse classification

class StateResolver:

    def __init__(self, instability_level):
        self.instability = instability_level

    def compute_stability_score(self, meaning, trust, time_pressure):
        """
        Stability = avg of:
        - meaning clarity (MR)
        - trust reliability (TR)
        - inverse instability
        - inverse time pressure
        """
        inst = 100 - self.instability
        tp = 100 - time_pressure
        return round((meaning + trust + inst + tp) / 4)

    def center_distance(self, stability_score):
        """Distance from ideal symmetry center."""
        return abs(50 - stability_score)

    def contradiction(self):
        """Contradiction magnitude C(x)."""
        return self.instability / 2

    def energy(self, D, C):
        """Collapse energy E(x)."""
        return D + C

    def classify_collapse(self, stability_score):
        """Categorize collapse output."""
        if stability_score >= 70:
            return "Stable Centered Collapse", "HIGH STABILITY (center-locked)"
        elif stability_score >= 40:
            return "Semi-Stable Collapse", "MID STABILITY (needs refinement)"
        else:
            return "Unstable / Premature Collapse", "LOW STABILITY (re-collapse likely)"

    def resolve(self, meaning, trust, time_pressure):
        """Compute full collapse-state result."""
        stability_score = self.compute_stability_score(
            meaning, trust, time_pressure
        )

        D = self.center_distance(stability_score)
        C = self.contradiction()
        E = self.energy(D, C)

        collapse_type, label = self.classify_collapse(stability_score)

        return {
            "stability_score": stability_score,
            "distance_from_center": D,
            "contradiction": C,
            "energy": E,
            "collapse_type": collapse_type,
            "label": label
        }
