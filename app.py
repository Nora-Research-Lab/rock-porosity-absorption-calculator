import gradio as gr
from rock_porosity_absorption_calculator import (
    calculate_absorption,
    calculate_porosity,
    calculate_bulk_density,
    classify_porosity
)

def compute(dry_weight, saturated_weight, submerged_weight):
    error_msg = ""
    try:
        dry = float(dry_weight)
        sat = float(saturated_weight)
        sub = float(submerged_weight)
    except (ValueError, TypeError):
        return "Please enter valid numeric weights.", "", "", ""

    if dry <= 0:
        error_msg = "Dry weight must be a positive number."
    elif sat <= dry:
        error_msg = "Saturated weight must be greater than dry weight."
    elif sub >= sat:
        error_msg = "Submerged weight must be less than saturated weight."
    if error_msg:
        return error_msg, "", "", ""

    absorption = calculate_absorption(dry, sat)
    porosity = calculate_porosity(dry, sat, sub)
    bulk_density = calculate_bulk_density(dry, sat, sub)
    classification = classify_porosity(porosity)
    result = (
        f"Water Absorption: {absorption:.2f}%",
        f"Apparent Porosity: {porosity:.2f}% — {classification}",
        f"Bulk Density: {bulk_density:.2f} g/cm³",
        ""
    )
    return result

reference_table = """
### Reference Ranges (Typical for Rocks)
| Property                | Very Low   | Low        | Moderate    | High       | Very High  |
|-------------------------|------------|------------|-------------|------------|------------|
| Apparent Porosity (%)   | <1         | 1 – 5      | 5 – 15      | 15 – 30    | >30        |
| Water Absorption (%)    | <0.5       | 0.5 – 2    | 2 – 6       | 6 – 12     | >12        |
| Bulk Density (g/cm³)    | >2.8       | 2.5 – 2.8  | 2.2 – 2.5   | 2.0 – 2.2  | <2.0       |
*Based on common engineering geology standards.*
"""

with gr.Blocks(title="Rock Porosity & Absorption Calculator") as demo:
    gr.Markdown("# Rock Porosity & Absorption Calculator")
    gr.Markdown("Enter weights in grams for calculation and classification.")
    with gr.Row():
        dry_input = gr.Number(label="Dry Weight (g)", value=250.0, precision=2)
        sat_input = gr.Number(label="Saturated Weight (g)", value=260.0, precision=2)
        sub_input = gr.Number(label="Submerged Weight (g)", value=150.0, precision=2)
    calc_btn = gr.Button("Calculate")
    with gr.Row():
        out_absorption = gr.Textbox(label="Water Absorption")
        out_porosity = gr.Textbox(label="Apparent Porosity & Classification")
    with gr.Row():
        out_bulkdensity = gr.Textbox(label="Bulk Density")
        out_reference = gr.Markdown(reference_table)
    calc_btn.click(
        fn=compute,
        inputs=[dry_input, sat_input, sub_input],
        outputs=[out_absorption, out_porosity, out_bulkdensity, out_reference]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
