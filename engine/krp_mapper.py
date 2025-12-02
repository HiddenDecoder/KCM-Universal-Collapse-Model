# KRP Mapper Module (KCM Engine)
# Author: Saurabh Misra (Karnav)
#
# This module isolates the KRP processing logic:
# MeaningRoot → RouteRoot → TrustRoot → TimeRoot
# This makes the engine modular, testable, and expandable.

class KRPMapper:
    """Processes input through the four KRP Roots (MR, RR, TR, TmR)."""

    def __init__(self, meaning, route, trust, time_pressure):
        self.meaning = meaning
        self.route = route
        self.trust = trust
        self.time_pressure = time_pressure

    def evaluate_meaning(self, signal):
        """MeaningRoot (MR) — clarity & semantic grounding."""
        return {
            "input": signal,
            "meaning_score": self.meaning,
            "comment": (
                "High clarity" if self.meaning >= 70 else
                "Moderate clarity" if self.meaning >= 40 else
                "Low clarity (reframe needed)"
            )
        }

    def evaluate_routes(self):
        """RouteRoot (RR) — available path width."""
        if self.route < 30:
            branch = "few narrow paths"
        elif self.route < 70:
            branch = "balanced number of paths"
        else:
            branch = "many competing paths"

        return {
            "route_score": self.route,
            "branching": branch
        }

    def evaluate_trust(self):
        """TrustRoot (TR) — structural consistency check."""
        if self.trust >= 70:
            msg = "High structural reliability"
        elif self.trust >= 40:
            msg = "Medium reliability"
        else:
            msg = "Low reliability (risk of collapse error)"

        return {
            "trust_score": self.trust,
            "trust_comment": msg
        }

    def evaluate_time(self):
        """TimeRoot (TmR) — urgency & pressure."""
        if self.time_pressure <= 30:
            tp = "Low time pressure"
        elif self.time_pressure <= 70:
            tp = "Moderate time pressure"
        else:
            tp = "High time pressure (premature collapse risk)"

        return {
            "time_pressure": self.time_pressure,
            "time_comment": tp
        }

    def full_krp_report(self, signal):
        """Returns complete KRP analysis for the engine."""
        return {
            "MR": self.evaluate_meaning(signal),
            "RR": self.evaluate_routes(),
            "TR": self.evaluate_trust(),
            "TmR": self.evaluate_time()
        }
