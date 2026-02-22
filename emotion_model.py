from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch


class ImageEmotionDetector:
    def __init__(self):
        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        )
        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        # 🔥 Much stronger prompts
        self.emotions = [
            "indian wedding ceremony",
            "wedding couple bride groom",
            "bride and groom marriage",
            "engagement ceremony",
            "romantic couple",
            "love couple",
            "birthday party",
            "dance party",
            "festival celebration",
            "sad moment",
            "happy celebration",
        ]

    def normalize_emotion(self, label: str):
        label = label.lower()

        if any(k in label for k in ["wedding", "bride", "groom", "marriage"]):
            return "wedding"

        if any(k in label for k in ["love", "romantic"]):
            return "love"

        if "birthday" in label:
            return "birthday"

        if any(k in label for k in ["party", "celebration", "dance", "festival"]):
            return "fun"

        if "sad" in label:
            return "sad"

        return "happy"

    # 🔥 MAJOR UPGRADE — top-k voting
    def detect_emotion(self, image: Image.Image):
        inputs = self.processor(
            text=self.emotions,
            images=image,
            return_tensors="pt",
            padding=True,
        )

        outputs = self.model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1)[0]

        # ⭐ TOP-3 instead of argmax
        topk = torch.topk(probs, k=3)

        labels = [self.emotions[i] for i in topk.indices.tolist()]

        # 🔥 Wedding priority check
        for lbl in labels:
            if any(k in lbl.lower() for k in ["wedding", "bride", "groom", "marriage"]):
                return "wedding"

        # fallback to best label
        return self.normalize_emotion(labels[0])