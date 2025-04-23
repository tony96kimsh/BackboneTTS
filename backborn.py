from pydub import AudioSegment
import speech_recognition as sr

# convert mp4 to wav
sound = AudioSegment.from_mp3("audio.mp3")
sound.export("converted.wav", format="wav")

# 음성 인식 준비
r = sr.Recognizer()
with sr.AudioFile("converted.wav") as source:
    audio = r.record(source)


# 텍스트 변환
try:
    text = r.recognize_google(audio, language="ko-KR")
    print("인식된 텍스트:\n", text)
except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError:
    print("Google API에 요청 실패")
