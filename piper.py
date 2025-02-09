# djm 2025/02
# 90% of this code is from Kalliope
# all can use

import wave
from piper.voice import PiperVoice
from kalliope.core.TTS.TTSModule import TTSModule, MissingTTSParameter

import logging
import sys

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Piper(TTSModule):

    def __init__(self, **kwargs):
        super(Piper, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.model = kwargs.get('model', None)

        self._check_parameters()

    def _check_parameters(self):
        """
        Check parameters are ok, raise MissingTTSParameters exception otherwise.
        :return: true if parameters are ok, raise an exception otherwise

               .. raises:: MissingTTSParameterException
        """
        if self.language == "default" or self.language is None:
            raise MissingTTSParameter("[Piper] Missing language, bad tts cache path !")
        return True

        if self.model is None:
            raise MissingTTSParameter("[Piper] Missing model, check documentation !")
        return True

    def say(self, words):
        """
        :param words: The sentence to say
        """

        self.generate_and_play(words, self._generate_audio_file)

    def _generate_audio_file(self):
        """
        Generic method used as a Callback in TTSModule
            - must provided the audio file and write it on the disk

        .. raises:: FailToLoadSoundFile
        """
        voice = PiperVoice.load(self.model)
        logger.debug("[Piper] File Path: %s" % self.file_path)
        wav_file = wave.open(self.file_path, "w")
        audio = voice.synthesize(self.words, wav_file)
        wav_file.close()
