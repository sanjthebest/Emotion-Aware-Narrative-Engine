import pytest
from emotion_engine import EmotionEngine

def test_emotion_engine_initialization():
    engine = EmotionEngine().initialize()
    assert engine is not None

def test_basic_emotion_detection():
    engine = EmotionEngine().initialize()
    result = engine.detect_emotion("I am so happy today!")
    assert 'emotion' in result
    assert 'confidence' in result

def test_scene_based_detection():
    engine = EmotionEngine().initialize()
    result = engine.detect_emotion("I am so happy today!", scene="romantic_date")
    assert 'emotion' in result
    assert 'mood_suggestion' in result

def test_context_override():
    engine = EmotionEngine().initialize()
    result = engine.detect_emotion("I am so happy today!", context="flirty")
    assert 'emotion' in result
    assert 'mood_suggestion' in result
