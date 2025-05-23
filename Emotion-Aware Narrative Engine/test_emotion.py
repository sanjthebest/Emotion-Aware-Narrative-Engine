from emotion_engine import EmotionEngine

def test_dialogue(engine, dialogue_data):
    """Helper function to test dialogue and print results"""
    print("\nTesting dialogue:")
    print(f"Text: {dialogue_data['text']}")
    print(f"Scene: {dialogue_data.get('scene', 'Not specified')}")
    print(f"Context: {dialogue_data.get('context', 'Not specified')}")
    
    result = engine.process_dialogue_file(dialogue_data)
    
    print("\nResults:")
    print(f"Original Emotion: {result['original_emotion']}")
    print(f"Final Emotion: {result['emotion']}")
    print(f"Scene Mood: {result['scene_mood']}")
    print(f"Intensity: {result['intensity']}")
    print(f"Mood Suggestion: {result['mood_suggestion']}")
    print("-" * 50)

def main():
    # Initialize the emotion engine
    engine = EmotionEngine().initialize()
    
    # Test cases
    test_cases = [
        # Test 1: Basic emotion detection
        {
            "text": "quit it",
            "scene": "casual_conversation"
        },
        
        # Test 2: Romantic scene with flirty context
        {
            "text": "quit it",
            "scene": "romantic_date",
            "context": "flirty"
        },
        
        # Test 3: Battle scene with angry context
        {
            "text": "quit it",
            "scene": "battle_scene",
            "context": "angry"
        },
        
        # Test 4: Casual conversation with flirty context
        {
            "text": "quit it",
            "scene": "casual_conversation",
            "context": "flirty"
        },
        
        # Test 5: Using scene alias
        {
            "text": "quit it",
            "scene": "date",  # This should match "romantic_date"
            "context": "flirty"
        }
    ]
    
    # Run all test cases
    for test_case in test_cases:
        test_dialogue(engine, test_case)

if __name__ == "__main__":
    main() 