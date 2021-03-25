from mod import State, Renderer, Controller
import config

state = State(
    config.Dimensions.HEIGHT,
    config.Dimensions.WIDTH)

renderer = Renderer(
    config.Dimensions.HEIGHT,
    config.Dimensions.WIDTH)

controller = Controller(state, renderer)

# Okay, the web app should have got ready now. Nothing else to do.