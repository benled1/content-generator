from media.audio import TextToSpeechChatTTS, IAudioGenerator, AudioMaker, Audio
from media.subtitle import ISubtitleGenerator, SubtitleGeneratorWhisperModel, SubtitleMaker, Subtitle

import uuid

"""
TODO:
- create a footage generator/maker class that will retrieve or gen footage in some way. abstract this out in the same way it was done for both subtitles and audio
- abstract away the method of uploading from the generator class. Generator should make and return the object with a reference to a local tmp file. Uploader/StorageManager should store the file
    in a more official place like s3 or a none tmp file like (local_media_store)
- create tests for each of the packages and their main functionality. This includes unit tests and integration tests. Integration tests should test the whole class like for example
    the Audio integration test would create a full audio file and then check to see if it is a valid .wav file or whatever the expected output is.


EXTRA TODO:
- put the uuid of the file as a property in the file class for ex. Audio.uuid should be a property. This way the subtitle doesn't have to retrieve the uuid from the file name.
"""


if __name__ == "__main__":
    
    chat_tts_audio_generator: IAudioGenerator = TextToSpeechChatTTS()
    audio_maker: AudioMaker  = AudioMaker(audio_generator=chat_tts_audio_generator)
    audio: Audio = audio_maker.make_audio("This is made with a audio generator and maker.")
    whisper_model_srt_generator : ISubtitleGenerator = SubtitleGeneratorWhisperModel()
    subtitle_maker: SubtitleMaker = SubtitleMaker(whisper_model_srt_generator)
    subtitle: Subtitle = subtitle_maker.make_subtitle(audio)
    

    






