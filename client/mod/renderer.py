from browser import document, html

from mod import state

class Renderer:
    '''Renders the web page.'''

    def __init__(self, height, width):
        self.guide = html.DIV("""Control Guide: C-c for copy, C-v for paste,
            Arrow keys / mouse click for moving the cursor.""")

        self.foot = html.DIV((
            "Made with ",
            html.A("Brython", href="http://www.brython.info"),
        ))

        self.button_clear = html.BUTTON("Clear")
        self.buttons = [
            self.button_clear,
        ]

        self.cells = [
            [html.TD(html.PRE(), row=i, col=j, chosen="no") for j in range(width)]
            for i in range(height)]

        self.root = document
        self.root <= (
            self.guide,
            html.DIV(self.buttons, id="buttons"),
            html.TABLE([html.TR(line) for line in self.cells],
                id="board"),
            self.foot,
        )

    def update(self, state_obj: 'state.State'):
        '''Updates the page according to the newest state.'''
        curr_board = state_obj.board
        curr_i, curr_j = state_obj.cursor

        # TODO: Time costly, will optimize
        for i in range(state_obj.height):
            for j in range(state_obj.width):
                cell = self.cells[i][j]
                # change char:
                char = curr_board[i][j] or ' '
                cell_text, = cell.select("pre")
                cell_text.text = char
                # change cursor state:
                if i == curr_i and j == curr_j:
                    cell["chosen"] = "yes"
                else:
                    cell["chosen"] = "no"
                    