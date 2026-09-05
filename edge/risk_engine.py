from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RiskResult:
    node_id: str
    node_type: str
    hazard: str
    risk_score: float
    confidence: float
    severity: str
    trend: str
    status: str
    action: str
    contributing_factors: List[str]


class RiskEngine:

    def __init__(self):
        self.history: Dict[str, List[float]] = {}

    def _clamp(self, value: float) -> float:
        return max(0.0, min(100.0, value))

    def _severity(self, score: float) -> str:
        if score >= 75:
            return "CRITICAL"

        if score >= 45:
            return "WARNING"

        return "NORMAL"

    def _trend(self, node_id: str, score: float) -> str:

        history = self.history.setdefault(node_id, [])

        if not history:
            trend = "STABLE"

        elif score > history[-1] + 5:
            trend = "RISING"

        elif score < history[-1] - 5:
            trend = "FALLING"

        else:
            trend = "STABLE"

        history.append(score)

        if len(history) > 10:
            history.pop(0)

        return trend

    def analyze(self, reading):

        if reading.node_type == "river":
            return self._analyze_flood(reading)

        if reading.node_type == "forest":
            return self._analyze_fire(reading)

        if reading.node_type == "urban":
            return self._analyze_pollution(reading)

        return RiskResult(
            node_id=reading.node_id,
            node_type=reading.node_type,
            hazard="UNKNOWN",
            risk_score=0.0,
            confidence=0.0,
            severity="NORMAL",
            trend="STABLE",
            status="NO_HAZARD",
            action="CONTINUE_MONITORING",
            contributing_factors=[]
        )

    # =========================================================
    # FLOOD ANALYSIS
    # =========================================================

    def _analyze_flood(self, reading):

        factors = []

        water_score = self._clamp(
            (reading.water_level - 30) / 60 * 100
        )

        rainfall_score = self._clamp(
            reading.rainfall / 60 * 100
        )

        soil_score = self._clamp(
            (reading.soil_moisture - 30) / 70 * 100
        )

        humidity_score = self._clamp(
            (reading.humidity - 50) / 50 * 100
        )

        if reading.water_level >= 70:
            factors.append("High water level")

        if reading.rainfall >= 40:
            factors.append("Heavy rainfall")

        if reading.soil_moisture >= 80:
            factors.append("High soil moisture")

        if reading.humidity >= 85:
            factors.append("High humidity")

        score = (
            water_score * 0.40
            + rainfall_score * 0.30
            + soil_score * 0.20
            + humidity_score * 0.10
        )

        confidence = self._clamp(
            55 + len(factors) * 10
        )

        return self._build_result(
            reading,
            "FLOOD",
            score,
            confidence,
            factors,
            "FLOOD RESPONSE ALERT"
        )

    # =========================================================
    # FIRE ANALYSIS
    # =========================================================

    def _analyze_fire(self, reading):

        factors = []

        temperature_score = self._clamp(
            (reading.temperature - 25) / 25 * 100
        )

        smoke_score = self._clamp(
            reading.smoke / 60 * 100
        )

        gas_score = self._clamp(
            reading.gas / 60 * 100
        )

        dryness_score = self._clamp(
            (70 - reading.humidity) / 50 * 100
        )

        if reading.temperature >= 38:
            factors.append("High temperature")

        if reading.smoke >= 20:
            factors.append("Smoke detected")

        if reading.gas >= 25:
            factors.append("Elevated gas concentration")

        if reading.humidity <= 40:
            factors.append("Low humidity")

        score = (
            temperature_score * 0.30
            + smoke_score * 0.40
            + gas_score * 0.15
            + dryness_score * 0.15
        )

        confidence = self._clamp(
            55 + len(factors) * 10
        )

        return self._build_result(
            reading,
            "FIRE",
            score,
            confidence,
            factors,
            "FIRE RESPONSE ALERT"
        )

    # =========================================================
    # POLLUTION ANALYSIS
    # =========================================================

    def _analyze_pollution(self, reading):

        factors = []

        pm25_score = self._clamp(
            reading.pm25 / 150 * 100
        )

        pm10_score = self._clamp(
            reading.pm10 / 200 * 100
        )

        gas_score = self._clamp(
            reading.gas / 60 * 100
        )

        if reading.pm25 >= 60:
            factors.append("Elevated PM2.5")

        if reading.pm10 >= 100:
            factors.append("Elevated PM10")

        if reading.gas >= 25:
            factors.append("Elevated gas concentration")

        score = (
            pm25_score * 0.45
            + pm10_score * 0.35
            + gas_score * 0.20
        )

        confidence = self._clamp(
            55 + len(factors) * 10
        )

        return self._build_result(
            reading,
            "AIR_POLLUTION",
            score,
            confidence,
            factors,
            "AIR QUALITY ALERT"
        )

    # =========================================================
    # RESULT GENERATION
    # =========================================================

    def _build_result(
        self,
        reading,
        hazard,
        score,
        confidence,
        factors,
        action
    ):

        score = round(self._clamp(score), 2)
        confidence = round(self._clamp(confidence), 2)

        severity = self._severity(score)
        trend = self._trend(reading.node_id, score)

        if severity == "NORMAL":

            status = "NO_HAZARD"
            final_action = "CONTINUE_MONITORING"

        elif severity == "WARNING":

            status = "MONITOR"
            final_action = action

        else:

            status = "ACTIVE"
            final_action = action

        return RiskResult(
            node_id=reading.node_id,
            node_type=reading.node_type,
            hazard=hazard,
            risk_score=score,
            confidence=confidence,
            severity=severity,
            trend=trend,
            status=status,
            action=final_action,
            contributing_factors=factors
        )