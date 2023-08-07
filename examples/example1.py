from psychopy import visual, core, event


def presentation_experiment():
    # Create a window for the presentation
    win = visual.Window(size=(800, 600), units='pix')

    # List of words to present
    words = ['Stimulus  1', 'Stimulus  2', 'Stimulus  3']

    # Create a text stimulus
    text_stimulus = visual.TextStim(win=win, text='', height=50)

    # Maximum time to respond (in seconds)
    response_max_time = 5.0

    # Data logging
    data = []

    # Present each word in the experiment
    for word in words:
        # Display the word in the text stimulus
        text_stimulus.text = word
        text_stimulus.draw()
        win.flip()

        # Get the start time of the presentation
        start_time = core.getTime()

        # Wait for the participant's response
        response = None
        response_time = 0.0
        while True:
            keys = event.getKeys(timeStamped=True)
            if keys:
                response, response_time = keys[0]
                break
            if core.getTime() - start_time > response_max_time:
                break
            core.wait(0.01)

        # Record word and response data
        data.append({'Word': word, 'Response': response, 'Reaction time': response_time})

    # Close Window
    win.close()

    # Print the collected data
    for d in data:
        print(d)
