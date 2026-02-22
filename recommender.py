import pandas as pd
from collections import Counter
from emotion_model import ImageEmotionDetector


class BollywoodRecommender:
    def __init__(self):
        self.df = pd.read_csv("songs_dataset.csv")
        self.detector = ImageEmotionDetector()

        self.wedding_keywords = [
            "wedding",
            "marriage",
            "bride",
            "groom",
            "shaadi",
            "mehndi",
            "baraat",
            "engagement",
        ]

    def analyze_images(self, images):
        emotions = []

        for img in images:
            emotion = self.detector.detect_emotion(img)
            emotions.append(emotion)

        # 🔥 majority voting across images
        if emotions:
            most_common = Counter(emotions).most_common(1)[0][0]
            return most_common

        return "happy"

    def recommend(self, images, keywords, prompt, duration):
        detected_emotion = self.analyze_images(images)

        prompt_text = (prompt or "").lower()
        keyword_set = set([k.lower().strip() for k in (keywords or [])])

        # 🔥 scoring
        def score_row(row):
            score = 0
            row_emotion = str(row["emotion"]).lower()
            row_keywords = str(row["keywords"]).lower()

            # strong emotion match
            if row_emotion == detected_emotion:
                score += 5

            # keyword overlap
            for tag in keyword_set:
                if tag in row_keywords:
                    score += 2

            # wedding boost from prompt
            if any(k in prompt_text for k in self.wedding_keywords):
                if row_emotion == "wedding":
                    score += 5

            return score

        self.df["score"] = self.df.apply(score_row, axis=1)
        best = self.df.sort_values("score", ascending=False).iloc[0]

        return {
            "song": best["song"],
            "emotion_detected": detected_emotion,
            "lyrics": best["lyrics_snippet"],
            "recommended_duration": duration,
        }