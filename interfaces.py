"""
Multi-Layer Brain Twin (MLBT) — Public Interfaces
Version 1.0 — July 2026
Author: Sarah LAZRI

PUBLIC ILLUSTRATIVE MODULE.

This file defines the abstract architecture contract of the MLBT engine:
the methods every implementation must expose, and the sequence in which
they are called. It contains NO proprietary logic — every method body
either raises NotImplementedError or is left to subclasses to define.

The confidential engine (context detection, layer-selection heuristics,
correlation-based analysis, cross-layer integration, resource allocation)
implements these interfaces internally and is available only to partners
under a signed NDA.
"""

from abc import ABC, abstractmethod
from enum import Enum


class ExecutionState(Enum):
    IDLE = "idle"
    STANDBY = "standby"
    ACTIVE = "active"
    HIGH_ACTIVITY = "high_activity"


class LayerInterface(ABC):
    """
    Abstract contract for a single biological layer
    (Molecular, Cellular, Tissue, Organ, System, Whole-organism).
    """

    name: str
    state: ExecutionState

    @abstractmethod
    def activate(self, context: str) -> str:
        """
        Activate this layer for the given context.
        Real activation logic (what data is loaded, how it is scored)
        is implementation-specific and confidential.
        """
        raise NotImplementedError

    @abstractmethod
    def standby(self) -> str:
        """Return this layer to a low-frequency observation state."""
        raise NotImplementedError

    @abstractmethod
    def contribute(self) -> dict:
        """
        Return this layer's contribution to the current analysis.
        The real contribution payload (features, scores, correlations)
        is confidential and not defined by this interface.
        """
        raise NotImplementedError


class BrainTwinEngineInterface(ABC):
    """
    Abstract contract for the MLBT orchestration engine.

    Any concrete implementation (public demo or confidential production
    engine) must expose this sequence of operations:
        1. detect_context
        2. select_layers
        3. process_layers
        4. integrate
        5. reset_to_standby
    """

    @abstractmethod
    def detect_context(self, query: str) -> str:
        """
        Identify the relevant biological context for a query.
        Real context-detection logic is proprietary and confidential.
        """
        raise NotImplementedError

    @abstractmethod
    def select_layers(self, context: str) -> list:
        """
        Decide which layers are relevant to the given context.
        Real selection heuristics are proprietary and confidential.
        """
        raise NotImplementedError

    @abstractmethod
    def process_layers(self, layers: list, context: str) -> None:
        """Activate and run the selected layers for the given context."""
        raise NotImplementedError

    @abstractmethod
    def integrate(self, layers: list) -> str:
        """
        Combine layer contributions into a unified response.
        Real cross-layer integration and correlation-based analysis
        are proprietary and confidential.
        """
        raise NotImplementedError

    @abstractmethod
    def reset_to_standby(self, layers: list) -> None:
        """Return processed layers to standby once analysis is complete."""
        raise NotImplementedError

    def process_query(self, query: str) -> str:
        """
        Public, non-overridable orchestration sequence.
        Concrete subclasses only need to implement the five steps above —
        this method fixes the order in which they are called.
        """
        context = self.detect_context(query)
        layers = self.select_layers(context)
        self.process_layers(layers, context)
        result = self.integrate(layers)
        self.reset_to_standby(layers)
        return result
