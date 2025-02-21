from django.shortcuts import render

# Create your views here.
import os
import whisper
from pyannote.audio import Pipeline
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Load Whisper model for transcription
whisper_model = whisper.load_model("base")

# Load Pyannote pipeline for diarization (replace 'your_hf_token' with a real token)
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="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")

@csrf_exempt
def transcribe_audio(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            audio_file_path = data.get("audio_file_path", "")

            if not audio_file_path:
                return JsonResponse({"error": "No audio file path provided."}, status=400)

            if not os.path.exists(audio_file_path):
                return JsonResponse({"error": "File not found"}, status=400)

            # Transcribe audio using Whisper
            transcription_result = whisper_model.transcribe(audio_file_path)

            # Apply speaker diarization
            diarization_result = pipeline(audio_file_path)

            # Format results
            transcription_output = []
            for segment in diarization_result.itertracks(yield_label=True):
                start, end, speaker = segment[0].start, segment[0].end, segment[2]
                spoken_text = next((entry['text'] for entry in transcription_result['segments'] if start <= entry['start'] <= end), "")
                transcription_output.append({
                    "start": start,
                    "end": end,
                    "speaker": speaker,
                    "text": spoken_text
                })

            return JsonResponse({"transcription": transcription_output})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)