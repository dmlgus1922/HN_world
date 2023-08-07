import whisper

model = whisper.load_model('base')

def transcribe(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    print(f'detected language: {max(probs, key=probs.get)}')
    
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

text = transcribe('../data/audio2.wav')
print(text)