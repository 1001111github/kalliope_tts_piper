# kalliope_tts_piper
Piper-TTS TTSModule for Kalliope. Refer to [rhasspy/piper](https://github.com/rhasspy/piper) for details 

##Installation:
```bash
kalliope - install --git-url https://github.com/1001111github/kalliope_tts_piper.git
```

You will need to download at least one voice model with it's config from [here]https://github.com/rhasspy/piper/blob/master/VOICES.md
Place the model and json config in the desired directory. Rename the json config to match "full_model_file_name".json

## Parameters

| parameter    | required | type    | default | choices                              | comment                    |
|--------------|----------|---------|---------|--------------------------------------|----------------------------|
| language     | Yes      | string  |         | "your_model_choice"                  | filename, without extension 
| model        | Yes      | string  |         | "path/your_model_choice.[onnx|tflite]| Full path to model file
| name         | No       | string  |'default'| Or any wake word                      | Relates voices to names used as trigger wake words 
| voiceN       | No       | string  |         | Any label that contains 'voice'       | Identifies a voice (language/model) related to a wake word
| languageN    | No       | string  |         | "your_model_choiceN"                  | filename, without extension for voice N
| modelN       | No       | string  |         | "path/your_model_choiceN.[onnx|tflite]| Full path to model file for voice N
| nameN        | No       | string  |         | Any wake word                         | Wake word associated with voice N 

| cache        | Yes      | BOOL    |         | 'True', 'False' 

## Example settings

```yaml
#

default_text_to_speech: "piper"
text_to_speech
  - piper:
      language: "en_US-hfc_male-medium"
      model: "resources/tts/en_US-hfc_male-medium.onnx"
      name: 'default'
      voice1: 
         language: "en_US-kristin-medium"
         model: "resources/tts/en_US-kristin-medium.onnx"
         name: "alexa"
      cache: True
```
