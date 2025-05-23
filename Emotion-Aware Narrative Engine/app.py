from emotion_engine import EmotionEngine

def print_contexts(engine):
    """Print all available contexts"""
    print("\nAvailable Contexts:")
    print("------------------")
    contexts = engine.get_available_contexts()
    current_type = None
    
    for context_type, context_name, description in contexts:
        if context_type != current_type:
            current_type = context_type
            print(f"\n{context_type.upper()}:")
        print(f"- {context_name}: {description}")

def main():
    print("Emotion Detection for Game Mood")
    print("Enter a line of dialogue or narration. The AI will detect the emotion and suggest a game mood cue.")
    print("Type 'quit' to exit.")
    print("Type 'contexts' to see all available contexts.")
    
    # Initialize the emotion engine
    engine = EmotionEngine().initialize()
    
    while True:
        print("\nEnter text (or 'quit' to exit, 'contexts' to see available contexts):")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if user_input.lower() == 'contexts':
            print_contexts(engine)
            continue
            
        if user_input:
            print("\nEnter context (or press Enter for no context):")
            context = input("> ").strip().lower()
            
            result = engine.detect_emotion(user_input, context if context else None)
            
            print(f"\nOriginal Emotion: {result['original_emotion'].title()} ({result['confidence']:.2f})")
            if result['original_emotion'] != result['emotion']:
                print(f"Context-Adjusted Emotion: {result['emotion'].title()}")
            print(f"Suggested Game Mood: {result['mood_suggestion']}")

if __name__ == "__main__":
    main()