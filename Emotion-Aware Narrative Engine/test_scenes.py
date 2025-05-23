from emotion_engine import EmotionEngine

def test_scene_detection():
    # Initialize the engine
    engine = EmotionEngine().initialize()
    
    # Test cases for different scene types
    test_cases = [
        # Social Scenes
        {
            "text": "I'm looking forward to our meeting tomorrow",
            "scene": "formal_meeting",
            "description": "Professional meeting anticipation"
        },
        {
            "text": "Let's celebrate this amazing achievement!",
            "scene": "party",
            "description": "Celebratory party moment"
        },
        {
            "text": "Mom, I missed your cooking so much",
            "scene": "family_gathering",
            "description": "Family reunion moment"
        },
        
        # Action Scenes
        {
            "text": "They're gaining on us, we need to move faster!",
            "scene": "chase_scene",
            "description": "Intense chase sequence"
        },
        {
            "text": "Stay quiet, we don't want to alert the guards",
            "scene": "stealth_mission",
            "description": "Stealth operation"
        },
        
        # Emotional Scenes
        {
            "text": "We'll always remember the good times we shared",
            "scene": "funeral",
            "description": "Funeral eulogy"
        },
        {
            "text": "I do",
            "scene": "wedding",
            "description": "Wedding vows"
        },
        
        # Mystery/Thriller Scenes
        {
            "text": "This clue doesn't make any sense",
            "scene": "investigation",
            "description": "Detective work"
        },
        {
            "text": "I know you're hiding something",
            "scene": "interrogation",
            "description": "Intense questioning"
        },
        
        # Fantasy/Sci-fi Scenes
        {
            "text": "The ancient magic flows through my veins",
            "scene": "magic_ritual",
            "description": "Magical ceremony"
        },
        {
            "text": "The quantum drive is failing!",
            "scene": "space_battle",
            "description": "Space combat crisis"
        }
    ]
    
    print("Testing Scene-Based Emotion Detection")
    print("====================================")
    
    for case in test_cases:
        print(f"\nTest Case: {case['description']}")
        print(f"Scene: {case['scene']}")
        print(f"Dialogue: '{case['text']}'")
        
        result = engine.detect_emotion(case['text'], scene=case['scene'])
        
        print(f"Original Emotion: {result['original_emotion'].title()} ({result['confidence']:.2f})")
        print(f"Scene Mood: {result['scene_mood'].title()}")
        print(f"Intensity: {result['intensity'].title()}")
        print(f"Mood Suggestion: {result['mood_suggestion']}")

if __name__ == "__main__":
    test_scene_detection() 