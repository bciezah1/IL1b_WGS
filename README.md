# Gene Ontology (GO) Enrichment Analysis Pipelines

This repository contains scripts and data (inputs and outputs) for performing GO and C2 collection enrichment analysis and other related tasks using single variant association and rare variant association from Ryan's work. The structure of the repository is organized to facilitate reproducibility and clarity.

**Note:** The scripts listed below were successfully tested on EUR and IL6, IL1b, and IL18. However, inputs and outputs included correspond only to EUR & IL6. For additional inputs and outputs, please, contact Basilio Cieza Huaman (bciezah@gmail.com).

---

## 1. `codes/`
This folder contains all the scripts used in the project, categorized by language:

### **Python**
- Scripts for GO terms extraction from supplementary material in Jung et al. (2021).

    - **`PDF_scrapping.py`**:  
      A custom Python script designed to extract GO terms from PDFs.  
      **Usage**: Provide the script with the PDF's location and the pages you want to extract data from.

### **R**
- Scripts for performing GO enrichment analysis and other pathway analyses.

    - **`Canonical_Pathway_Enrichment_Analysis.Rmd`**:  
      A custom R Markdown script for performing Canonical Pathway enrichment analysis using single variant and rare variant association outputs.
      
    - **`Canonical_Pathway_Enrichment_Analysis.html`**:  
      The HTML output from the above R script.

    - **`Gene_Ontology_Enrichment_Analysis.Rmd`**:  
      A custom R Markdown script for performing Gene Ontology enrichment analysis using single variant and rare variant association outputs.

    - **`Gene_Ontology_Enrichment_Analysis.html`**:  
      The HTML output from the above R script.

---

## 2. `inputs/`
This folder contains the input data used for the analysis, categorized by study type:

- **`rare_var/`**:  
  Contains input files for rare variant analysis.
  
- **`single_marker/`**:  
  Contains input files for single marker analysis.

---

## 3. `outputs/`
This folder contains the results of the analyses, organized by study type:

- **`rare_var/`**:  
  Contains output files for the Gene Ontology and C2 Collection for the rare variant analysis.
  
- **`single_marker/`**:  
  Contains output files for the Gene Ontology and C2 Collection for the single marker analysis.

---

## Data Provenance
The input data in the `inputs/` folder originates from Ryan's work.  
The outputs in the `outputs/` folder are generated using these inputs and the scripts in the `codes/` directory.

---

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to Ryan for providing the input data used in this project.

## Author

**Basilio Cieza Huaman**  
- PhD from Johns Hopkins University.    
- Email: bciezah@gmail.com  


