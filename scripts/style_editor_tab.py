import modules.scripts as scripts
import gradio as gr
import os

from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:

        with gr.Row():
            styles = gr.Dropdown(
                choices=["Choice 1", "Choice 2", "Choice 3", "Choice 4", "Choice 5"],
                show_label=True
            )
            angle = gr.Slider(
                minimum=0.0,
                maximum=360.0,
                step=1,
                value=0,
                label="Angle"
            )
            checkbox = gr.Checkbox(
                False,
                label="Checkbox"
            )
        return [(ui_component, "Extension Template", "extension_template_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)