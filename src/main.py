from audio_gen.tts_generator import TTSGenerator 
from audio_gen.subtitle_generator import SubtitleGenerator


if __name__ == "__main__":
    # tts_gen = tts_generator.TTSGenerator("./local_media_store/audio")
    # tts_gen.generate_audio_file("Once upon a time, in a world filled with holographic screens and virtual reality, there lived a young girl named Zara. She was part of Generation Alpha, the first generation to grow up with AI assistants and self-driving cars. Zara was curious, always tinkering with gadgets and exploring new apps that let her experience different realities.")
    subtitle_generator = SubtitleGenerator()
    subtitle_generator.transcribe_audio("./local_media_store/audio/test_audio.wav")



