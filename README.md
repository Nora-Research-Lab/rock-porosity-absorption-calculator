![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Rock Porosity & Absorption Calculator
 
*For engineering geologists and geotechnical engineers: enter dry, saturated, and submerged weights of a rock sample to instantly compute water absorption, apparent porosity, and bulk density.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Engineering Geology
 
The tool provides classic rock physical property measurements used in engineering geology and geotechnical practice. Inputs: (1) Dry weight in grams (positive number), (2) Saturated weight in grams (must be greater than dry), (3) Submerged weight in grams (must be less than saturated). Calculations: Water absorption (%) = ((saturated - dry) / dry) × 100. Apparent porosity (%) = ((saturated - dry) / (saturated - submerged)) × 100. Bulk density (g/cm³) = dry weight / (saturated - submerged). All weights in same units (g). The tool also classifies porosity: very low (<1%), low (1-5%), moderate (5-15%), high (15-30%), very high (>30%). UI: three numeric input fields with clear labels and units, a 'Calculate' button, and an output section displaying the three computed values with 2 decimal places, plus a classification text (e.g., 'Porosity: 8.3% — Moderate'). There is no AI component; it is a deterministic physical calculation. The tool also includes a small table summarizing typical ranges for reference.
 
## Run it
 
```bash
docker build -t rock-porosity-absorption-calculator .
docker run -p 7860:7860 rock-porosity-absorption-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-10-02.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
