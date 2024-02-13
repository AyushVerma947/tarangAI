from pydub import AudioSegment

def get_audio_frequency(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        frequency = audio.frame_rate
        return frequency
    except Exception as e:
        return str(e)
