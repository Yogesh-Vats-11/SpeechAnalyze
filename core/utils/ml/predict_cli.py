from predict import predict_speech

while True:
    jitter = float(input("\nEnter Jitter (%): "))
    shimmer = float(input("Enter Shimmer (%): "))
    wpm = float(input("Enter Words per Minute: "))
    pauses = float(input("Enter Pauses Duration (sec): "))

    features = [jitter, shimmer, wpm, pauses]

    predicted_label = predict_speech(features)  
    print(f"Predicted Severity of Defect: {predicted_label}")

    continue_input = input("\nDo you want to make another prediction? (y/n): ").lower()
    if continue_input != 'y':
        break

print("Goodbye!")
