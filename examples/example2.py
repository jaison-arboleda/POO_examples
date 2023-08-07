from psychopy import visual, core, event


class Experiment:

    def __init__(self):
        self.win = visual.Window(size=(800, 600), units='pix')
        self.text_stimulus = visual.TextStim(win=self.win, text='', height=50)
        self.response_max_time = 5.0
        self.data = []

    def present_word(self, word):
        self.text_stimulus.text = word
        self.text_stimulus.draw()
        self.win.flip()

        start_time = core.getTime()
        response = "N/A"
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
