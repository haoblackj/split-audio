import sys
import librosa
from pydub import AudioSegment
from pydub.silence import split_on_silence

# 引数から音声ファイルパスを取得
file_path = sys.argv[1]

# 音声ファイルを読み込む
audio, sr = librosa.load(file_path, sr=None)

# 音声ファイルの長さを取得
duration = librosa.get_duration(y=audio, sr=sr)

# pydub用にAudioSegmentオブジェクトに変換
audio_segment = AudioSegment.from_wav(file_path)

# 音声ファイルを発話単位に分割
chunks = split_on_silence(
    audio_segment,
    min_silence_len=500,  # 無音の最小長さ（ミリ秒）
    silence_thresh=-40    # 無音と判断する音量閾値（dBFS）
)

# 分割した発話を個別のファイルに保存
for i, chunk in enumerate(chunks):
    chunk.export(f"output/speech_{i}.wav", format="wav")