import pytest
from emotion_engine import EmotionEngine

@pytest.fixture
def engine():
    return EmotionEngine().initialize()
