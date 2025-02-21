## **Curr8labs submission**

I am hereby submitting my project based on the feature requirements in the mail.

To create a Python virtual environment, run:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Please install Django, openai-whisper, pyannote.audio, and openai>1.0.

Navigate into `myproject`:

```bash
cd myproject
```

Start the server:

```bash
python manage.py runserver
```

Use Postman to test out the endpoints.

# Feature 1:

use the endpoint assuming the server starts on 127.0.0.1:8000:

```bash
http://127.0.0.1:8000/api/generate-transcript/
```

provide the json body using

```bash
{
  "audio_file_path": "path/to/your/audio/file"
}
```

requirements: please add your pyannote/speaker-diarization access token from hugging face in audio_transcript/views.py line 15. please get access to this by providing simple details to
 - https://huggingface.co/hicustomer/pyannote-speaker-diarization
 - https://huggingface.co/philschmid/pyannote-segmentation

Heads-up: for initial setup wait for some time for the model to load from the net, and after running the endpoint please wait for 5-8 mins as the diarization takes time to process


# Feature 2:

use the endpoint assuming the server starts on 127.0.0.1:8000:

```bash
http://127.0.0.1:8000/api/generate-transcript/
```

provide the json body using

```bash
{
  "content": "your blog content"
}
```

requirements: please add your openai access token in blog/views.py line 6

Heads-up: please check with your openai account if your api limits are not exceeded, as this could create an issue

