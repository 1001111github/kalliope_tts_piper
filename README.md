# kalliope_tts_piper
Piper-TTS TTSModule for Kalliope<br/>
<p>Refer to https://github.com/rhasspy/piper for details </p>

<b>Installation:</b>
<p>pip install piper-tts<br/>
Create a directory piper in kalliope/tts<br/>
Copy all the .py files into kalliope/tts/piper<br/>
You will need to download at least one voice model with it's config from https://github.com/rhasspy/piper/blob/master/VOICES.md<BR/>
Place the model and json config in the desired directory. Rename the json config to match "full_model_file_name".json</p>

In settings.yml add the following to the text_to_speech section<br/>
<pre>
default_text_to_speech: "piper"

text_to_speech
  - piper:
      language: "your_model_choice"
      model: "resources/tts/your_model_choice.onnx"
      cache: True
</pre>

