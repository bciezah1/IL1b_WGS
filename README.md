# Gene Ontology (GO) Enrichment Analysis Pipeline

This repository contains scripts and data for performing GO enrichment analysis and other related tasks. The structure of the repository is organized to facilitate reproducibility and clarity.

---

## Repository Structure

The repository is organized into the following main directories:

### 1. `codes/`
This folder contains all the scripts used in the project, categorized by language:

- **`python/`**: Python scripts for data preprocessing, analysis, or visualization.
- **`R/`**: R scripts for statistical analysis and GO enrichment.

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

