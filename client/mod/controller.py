from mod import state, renderer

class Controller:
    '''Handles the input from mouse clicks and keyboard.'''

    # Wrapper:
    def will_update(func):
        '''Wrapper. Notify the renderer that state has been modified.'''
        def state_mutating_func(self: 'Controller', *args, **kwargs):
            ret = func(self, *args, **kwargs)
            self.renderer.update(self.state)
            return ret
        return state_mutating_func

    # Init function:
    @ will_update
    def __init__(self, state_obj: 'state.State', renderer_obj: 'renderer.Renderer'):
        self.state = state_obj
        self.renderer = renderer_obj

        for row in self.renderer.cells:
            for cell in row:
                cell.bind("click", self.on_cell_clicked)
        self.renderer.button_clear.bind("click", self.on_clear_button_clicked)

        self.renderer.root.bind("copy", self.on_copy)
        self.renderer.root.bind("paste", self.on_paste)

        # Refer to http://keycode.info/ for key names!
        self.key_actions = {
            "Delete": self.on_key_delete_,
            "Backspace": self.on_key_backspace_,
            "ArrowUp": self.on_key_uparrow_,
            "ArrowDown": self.on_key_downarrow_,
            "ArrowLeft": self.on_key_leftarrow_,
            "ArrowRight": self.on_key_rightarrow_,
        }
        self.renderer.root.bind("keydown", self.on_keydown)

    # Handling the mouse clicks:
    @ will_update
    def on_cell_clicked(self, event):
        cell = event.currentTarget # event.target is incorrect; might return a child
        i, j = int(cell["row"]), int(cell["col"])
        self.state.set_cursor_at(i, j)

    @ will_update
    def on_clear_button_clicked(self, event):
        self.state.clear_board()

    # Handing copy & paste operations
    def on_copy(self, event):
        text = self.state.copy_to_string()
        event.clipboardData.setData("text/plain", text)
        event.preventDefault()

    @ will_update
    def on_paste(self, event):
        text = event.clipboardData.getData("text/plain")
        self.state.paste_from_string(text)
        event.preventDefault()

    # Handling the keyboard:
    def on_key_normal_(self, char):
        self.state.put_char_and_proceed_cursor(char)

    def on_key_delete_(self):
        self.state.reset_char()

    def on_key_backspace_(self):
        self.state.move_cursor_by(0, -1)
        self.state.reset_char()

    def on_key_uparrow_(self):
        self.state.move_cursor_by(-1, 0)

    def on_key_downarrow_(self):
        self.state.move_cursor_by(+1, 0)

    def on_key_leftarrow_(self):
        self.state.move_cursor_by(0, -1)

    def on_key_rightarrow_(self):
        self.state.move_cursor_by(0, +1)

    @ will_update
    def on_keydown(self, event):
        if event.ctrlKey:
            return
        if len(event.key) == 1:
            self.on_key_normal_(event.key)
        elif event.key in self.key_actions:
            self.key_actions[event.key]()
        