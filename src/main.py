from audio_gen.audio_generator import AudioGenerator

if __name__ == "__main__":
    audio_generator = AudioGenerator()
    wav_file, srt_file = audio_generator.generate_audio("This is test text and it is funny smile")
    print(wav_file)
    print(srt_file)





