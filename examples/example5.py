from psychopy import visual, core, event, sound
from abc import ABC, abstractmethod


# multiple inheritance
# abstract class
class Stimulus(ABC):
    def __init__(self, win):
        self.win = win

    @abstractmethod
    def show(self, *args):
        pass


class StimulusText(Stimulus):
    def __init__(self, win, text):
        super().__init__(win)
        self.stimulus = visual.TextStim(win=self.win, text='', height=50)
        self.text = text

    def show(self):
        self.stimulus.text = self.text
        self.stimulus.draw()


class Experiment:
    def __init__(self):
        self.win = visual.Window(size=(800, 600), units='pix')
        # ,self.stimulus = StimulusText(self.win, 'Text of a stimulus')
        self.response_max_time = 2.0
        self.data = []

    def get_response(self, start_time):
        response = None
        response_time = 0.0
        while True:
            keys = event.getKeys(timeStamped=True)
            if keys:
                response, response_time = keys[0]
                break
            if core.getTime() - start_time > self.response_max_time:
                break
            core.wait(0.01)
        return response, response_time

    def present_stimulus(self, stimulus):
        stimulus.show()
        self.win.flip()

        start_time = core.getTime()
        response, response_time = self.get_response(start_time)
        return response, response_time

    def perform_experiment(self, stimuli):
        for stimulus in stimuli:
            response, response_time = self.present_stimulus(stimulus)
            self.data.append({'Stimuli': stimulus.__class__.__name__, 'Response': response,
                              'Reaction time': response_time})

    def print_data(self):
        # Print the collected data
        for d in self.data:
            print(d)

    def close_window(self):
        self.win.close()


class StimuloAudio(Stimulus, Experiment):
    def __init__(self, win):
        super().__init__(win)
        self.duration_tone = 2.0

    def show(self):
        # Logic for displaying the audio stimulus
        tone = sound.Sound('440')
        tone.play()
        core.wait(self.duration_tone)
        tone.stop()


def start_experiment():
    experiment = Experiment()
    text_stimulus = StimulusText(experiment.win, 'Text of a stimulus')
    audio_stimulus = StimuloAudio(experiment.win)

    experiment.perform_experiment([text_stimulus, audio_stimulus])
    experiment.print_data()
    experiment.close_window()
