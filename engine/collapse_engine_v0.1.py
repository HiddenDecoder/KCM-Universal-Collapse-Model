# KCM Collapse Engine v0.1
# Author: Saurabh Misra (Karnav)
#
# This file implements the first functional version of the Karnav Collapse Model (KCM)
# collapse engine. It is a simplified, runnable demonstration of:
#   - KRP Roots (MR, RR, TR, TmR)
#   - Stability Energy computation
#   - Collapse Rule: x* = argmin E(x)
#   - Final Center-aligned decision output

class KRPRoots:
    """KRP Root System (MR → RR → TR → TmR)"""

    def __init__(self, meaning, route, trust, time_pressure):
        self.meaning = meaning          # MeaningRoot clarity score (0–100)
        self.route = route              # RouteRoot option-width score (0–100)
        self.trust = trust              # TrustRoot structural reliability (0–100)
        self.time_pressure = time_pressure  # TimeRoot urgency (0–100)

    def summary(self):
        return {
            "MR": self.meaning,
            "RR": self.route,
            "TR": self.trust,
            "TmR": self.time_pressure
        }


class KCMMath:
    """Mathematical layer handling stability energy."""

    @staticmethod
    def center_distance(stability_score):
        # pseudo-distance from perfect center (50 = neutral midpoint)
        return abs(50 - stability_score)

    @staticmethod
    def contradiction(instability):
        # direct contradiction proxy
        return instability / 2

    @staticmethod
    def energy(D, C):
        # E(x) = D(x) + C(x)
        return D + C


class KCMCollapseEngine:
    """Main collapse engine implementing the 1 → C → 0 transformation."""

    def __init__(self, signal_text, krp: KRPRoots, instability_level):
        self.signal = signal_text.strip()
        self.krp = krp
        self.instability = instability_level

    def compute_stability_score(self):
        """
        Stability Score = average of:
        MR clarity, TR reliability, (100 - instability), (100 - time pressure).
        """
        MR = self.krp.meaning
        TR = self.krp.trust
        inst = 100 - self.instability
        tp = 100 - self.krp.time_pressure

        return round((MR + TR + inst + tp) / 4)

    def collapse(self):
        """Runs the entire collapse pipeline."""

        stability_score = self.compute_stability_score()

        # collapse math
        D = KCMMath.center_distance(stability_score)
        C = KCMMath.contradiction(self.instability)
        E = KCMMath.energy(D, C)

        # collapse classification
        if stability_score >= 70:
            collapse_type = "Stable Centered Collapse"
            label = "HIGH STABILITY (center-locked)"
        elif stability_score >= 40:
            collapse_type = "Semi-Stable Collapse"
            label = "MID STABILITY (needs refinement)"
        else:
            collapse_type = "Unstable / Premature Collapse"
            label = "LOW STABILITY (re-collapse likely)"

        return {
            "input": self.signal if self.signal else "[No input text provided]",
            "krp": self.krp.summary(),
            "instability": self.instability,
            "stability_score": stability_score,
            "distance_from_center": D,
            "contradiction": C,
            "energy": E,
            "collapse_type": collapse_type,
            "label": label
        }


# ---------------------------------------------------------------------
# Example usage (this section shows how the engine works)
# Remove or comment out before integrating into a larger system.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Sample parameters (modifiable)
    signal = "A startup must choose between fast growth or stable growth."
    krp = KRPRoots(
        meaning=70,
        route=60,
        trust=65,
        time_pressure=50
    )
    instability = 55

    engine = KCMCollapseEngine(signal, krp, instability)
    result = engine.collapse()

    print("\n--- KCM Collapse Engine Output ---")
    for key, value in result.items():
        print(f"{key}: {value}")
