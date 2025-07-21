from google import genai
My_api_key = ""  #NEVER DISCLOSE OR HARDCODE YOUR API_KEY 
client = genai.Client(api_key=My_api_key)

response  = client.models.generate_content(
    model="gemini-2.5-flash",contents="Tell Me how Artificial intelligence works in simple words"
)
print(response.text)

'''
SAMPLE RESPONSE

1.  **Feeding it Information (Data):**
    *   Just like a child learns by seeing, hearing, and experiencing things, AI learns by being given **lots and lots of information** (we call this "data").
    *   This data can be pictures, words, numbers, sounds, videos, or anything that can be put into a computer.
    *   *Example:* If you want AI to recognize a cat, you show it thousands of pictures of cats (and also dogs, birds, etc., so it learns what *isn't* a cat).

2.  **Finding Patterns (Learning):**
    *   The AI's "brain" (which is a very complex computer program) then looks for **patterns and relationships** within that data.
    *   It tries to figure out what makes a "cat" a "cat" – maybe it's the pointy ears, the whiskers, the shape of the eyes, etc.
    *   *Example:* It learns that pictures labeled "cat" often have certain visual features in common.

3.  **Making Decisions or Predictions (Applying Knowledge):**
    *   Once the AI has learned these patterns, it can then use them to do new things or make "smart guesses" when it sees *new* information it hasn't seen before.
    *   *Example:* If you show the AI a brand new picture, it can now say, "That's a cat!" or "That's a dog!" based on the patterns it learned.

4.  **Learning from Mistakes (Improving):**
    *   The cool thing is, AI also learns from its mistakes.
    *   If it guesses wrong (e.g., says a dog is a cat), a human or more data can correct it. The AI then adjusts its internal patterns to do better next time.
    *   It's like practicing – the more it practices with data and gets feedback, the smarter and more accurate it becomes.

**In essence:**

*   **AI eats data.**
*   **It finds patterns in that data.**
*   **It uses those patterns to make smart decisions or predictions about new information.**
*   **It keeps getting better over time by learning from its errors and more data.**

Think of it in action:

*   **Siri or Alexa:** They learned patterns of human speech to understand your commands.
*   **Netflix or Spotify:** They learned patterns in your viewing/listening habits to recommend new shows/songs you might like.
*   **Self-driving cars:** They learned patterns from millions of miles of driving data to recognize traffic lights, pedestrians, and other cars.
*   **Spam filters:** They learned patterns in emails to identify what's junk and what's legitimate.
'''
