def format_message(text, emotion):

    if emotion == "joy":
        return f"😊 {text} That's wonderful!"

    elif emotion == "sadness":
        return f"💙 {text} I truly appreciate your understanding."

    elif emotion == "anger":
        return f"⚠️ {text} Let's try to resolve this calmly."

    elif emotion == "fear":
        return f"😟 {text} Everything will be okay."

    elif emotion == "surprise":
        return f"😮 {text} That was unexpected!"

    elif emotion == "disgust":
        return f"😕 {text}"

    else:
        return text