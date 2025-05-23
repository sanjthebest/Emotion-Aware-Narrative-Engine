from emotion_engine import EmotionEngine

def test_context_scene_interaction():
    # Initialize the engine
    engine = EmotionEngine().initialize()
    
    # Test cases combining scenes and contexts
    test_cases = [
        # Romantic Context Tests
        {
            "text": "quit it",
            "scene": "romantic_date",
            "context": "flirty",
            "description": "Flirty context in romantic scene"
        },
        {
            "text": "quit it",
            "scene": "battle_scene",
            "context": "flirty",
            "description": "Flirty context in battle scene"
        },
        
        # Angry Context Tests
        {
            "text": "I'm so happy to see you",
            "scene": "casual_conversation",
            "context": "angry",
            "description": "Angry context in casual scene"
        },
        {
            "text": "I'm so happy to see you",
            "scene": "formal_meeting",
            "context": "angry",
            "description": "Angry context in formal scene"
        },
        
        # Complex Scene-Context Combinations
        {
            "text": "I can't believe you did this",
            "scene": "interrogation",
            "context": "flirty",
            "description": "Flirty context in interrogation scene"
        },
        {
            "text": "I can't believe you did this",
            "scene": "romantic_date",
            "context": "angry",
            "description": "Angry context in romantic scene"
        },
        
        # Emotional Scene Tests
        {
            "text": "I'm so excited",
            "scene": "funeral",
            "context": "flirty",
            "description": "Flirty context in funeral scene"
        },
        {
            "text": "I'm so excited",
            "scene": "wedding",
            "context": "angry",
            "description": "Angry context in wedding scene"
        },
        
        # Action Scene Tests
        {
            "text": "Let's get out of here",
            "scene": "chase_scene",
            "context": "flirty",
            "description": "Flirty context in chase scene"
        },
        {
            "text": "Let's get out of here",
            "scene": "stealth_mission",
            "context": "angry",
            "description": "Angry context in stealth scene"
        }
    ]
    
    print("Testing Context-Scene Interaction")
    print("================================")
    
    for case in test_cases:
        print(f"\nTest Case: {case['description']}")
        print(f"Scene: {case['scene']}")
        print(f"Context: {case['context']}")
        print(f"Dialogue: '{case['text']}'")
        
        # Test without context first
        base_result = engine.detect_emotion(case['text'], scene=case['scene'])
        print("\nBase Result (Scene Only):")
        print(f"Original Emotion: {base_result['original_emotion'].title()} ({base_result['confidence']:.2f})")
        print(f"Scene Mood: {base_result['scene_mood'].title()}")
        
        # Test with context
        context_result = engine.detect_emotion(case['text'], scene=case['scene'], context=case['context'])
        print("\nWith Context:")
        print(f"Original Emotion: {context_result['original_emotion'].title()} ({context_result['confidence']:.2f})")
        print(f"Final Emotion: {context_result['emotion'].title()}")
        print(f"Scene Mood: {context_result['scene_mood'].title()}")
        print(f"Intensity: {context_result['intensity'].title()}")
        print(f"Mood Suggestion: {context_result['mood_suggestion']}")
        print("-" * 50)

if __name__ == "__main__":
    test_context_scene_interaction() 
