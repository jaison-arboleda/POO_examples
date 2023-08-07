from psychopy import visual, core, event


# We use The principle of separation of responsibilities (SOLID)
class StimulusText:
    def __init__(self, win):
        self.stimulus = visual.TextStim(win=win, text='', height=50)

    def show(self, text):
        self.stimulus.text = text
        self.stimulus.draw()


class Experiment:
    def __init__(self):
        self.win = visual.Window(size=(800, 600), units='pix')
        self.stimulus_text = StimulusText(self.win)
        self.max_time_response = 2.0
        self.data = []

    def get_response(self, start_time):
        response = "N/A"
        response_time = 0.0
        while True:
            keys = event.getKeys(timeStamped=True)
            if keys:
                response, response_time = keys[0]
                break
            if core.getTime() - start_time > self.max_time_response:
                break
            core.wait(0.01)
        return response, response_time

    def present_word(self, word):
        self.stimulus_text.show(word)
        self.win.flip()

        start_time = core.getTime()
        response, response_time = self.get_response(start_time)
        return response, response_time

    def perform_experiment(self, words):
        for word in words:
            response, response_time = self.present_word(word)
            self.data.append({'Word': word, 'Response': response, 'Reaction time': response_time})

    def print_data(self):
        # Print the collected data
        for d in self.data:
            print(d)

    def close_window(self):
        self.win.close()


def start_experiment():
    words = ['Stimulus  1', 'Stimulus  2', 'Stimulus  3']

    experiment = Experiment()
    experiment.perform_experiment(words)
    experiment.close_window()
    experiment.print_data()
