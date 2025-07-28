from deepface import DeepFace
import tempfile

def analyze_emotion(image_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image_file.save(tmp.name)
        result = DeepFace.analyze(img_path=tmp.name, actions=["emotion"])
        return result[0]["emotion"]
