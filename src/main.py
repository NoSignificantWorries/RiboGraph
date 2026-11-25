import panel as pn
from urllib.parse import urlencode

pn.extension()

sequence_input = pn.widgets.TextInput(
    name="RNA sequence",
    value="AACGUUAGUU"
)

structure_input = pn.widgets.TextInput(
    name="Dot-bracket structure",
    value="(((....)))"
)

viewer = pn.pane.HTML(
    "",
    height=650,
    sizing_mode="stretch_width"
)

def update_structure(event=None):
    sequence = sequence_input.value
    structure = structure_input.value

    if len(sequence) != len(structure):
        return

    params = urlencode({
        "id": "url/my_rna",
        "sequence": sequence,
        "structure": structure
    })

    url = (
        "https://nibiru.tbi.univie.ac.at/forna/forna.html?"
        + params
    )

    viewer.object = f'''
    <iframe
        src="{url}"
        width="100%"
        height="630"
        frameborder="0">
    </iframe>
    '''

button = pn.widgets.Button(
    name="Update structure",
    button_type="primary"
)

button.on_click(update_structure)

app = pn.Column(
    "## RNA secondary structure",
    sequence_input,
    structure_input,
    button,
    viewer
)

app.servable()

