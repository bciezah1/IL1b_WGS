# Gene Ontology (GO) Enrichment Analysis Pipelines

This repository contains scripts and data for performing GO and C2 collection enrichment analysis and other related tasks using single variant association and rare variant association from Ryan's work. The structure of the repository is organized to facilitate reproducibility and clarity.

---

## Repository Structure

The repository is organized into the following main directories:

### 1. `codes/`
This folder contains all the scripts used in the project, categorized by language:

- **`python/`**: Python scripts for GO terms extraction from supplementary (PDF) in Jung et al (2021).
        - PDF_scrapping.py: A custom python script to extract GO terms. It only need the location of the PDF and the pages you want to extract data from.
- **`R/`**: R scripts to perform GO and C2, C3, C4, C5, C6, and C7 enrichment analysis.
        - Canonical_Pathway_Enrichment_Analysis.Rmd
        - Canonical_Pathway_Enrichment_Analysis.html
        - Gene_Ontology_Enrichment_Analysis.Rmd
        - Gene_Ontology_Enrichment_Analysis.html

---

### 2. `inputs/`
This folder contains input data, organized by study type:

- **`rare_var/`**: Input files related to rare variant analysis.
- **`single_marker/`**: Input files related to single marker analysis.

All input data files were provided by Ryan's work.

---

### 3. `outputs/`
This folder contains the results of analyses, generated using the scripts in `codes/` and data from `inputs/`. The results are organized by study type:

- **`rare_var/`**: Output files for rare variant analysis.
- **`single_marker/`**: Output files for single marker analysis.

---

## Data Source

The input files in the `inputs/` folder are derived from Ryan's work. The outputs are created using these inputs and the scripts in the `codes/` folder.

---

## How to Use

1. **Navigate to the `codes/` folder** and locate the script(s) you wish to run.
2. **Ensure input files are placed in the appropriate subdirectories** under `inputs/`.
3. **Run the scripts**, specifying the correct paths for input and output files if required.
4. **Check the `outputs/` folder** for results, organized by study type.

---

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to Ryan for providing the input data used in this project.

