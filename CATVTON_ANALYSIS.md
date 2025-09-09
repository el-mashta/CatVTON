# Plan: Surgical API-Level Dependency Audit for CatVTON

This document outlines a systematic, four-phase plan to analyze the dependencies of the `CatVTON` repository. The primary goal is to produce a minimal, verified `requirements.txt` file that allows for a safe and targeted upgrade of the `diffusers` library (and its core dependencies) while ensuring the rest of the complex, vendored code continues to function correctly.

The strategy is to perform a detailed, API-level audit by programmatically extracting the exact functions and classes being imported from each external library. This replaces guesswork with data, providing a high degree of confidence in the final proposed changes.

---

### **Phase 1: File Discovery (Estimated Time: 2 minutes)**

*   **Action:** The first step is to map the entire Python codebase. I will execute a `glob` search to get a complete list of all `.py` files within the `CatVTON` directory.
*   **Outcome:** A definitive list of all Python source files that need to be analyzed for their dependencies.

---

### **Phase 2: Automated API Usage Extraction (Estimated Time: 15-20 minutes)**

*   **Action:** This is the core data-gathering phase. I will execute a series of parallel `search_file_content` calls with specific, robust regular expressions to extract not just the modules, but the precise classes and functions being imported.
*   **Regex Patterns to be Used:**
    1.  `^import ([\w.]+)`: To capture top-level module imports (e.g., `import torch`).
    2.  `^from ([\w.]+) import \(?([^)]+)\)?`: To capture specific member imports (e.g., `from PIL import Image, ImageOps`), correctly handling both single-line and multi-line parenthesized imports.
*   **Data Aggregation:** The raw output from the search will be programmatically processed into a structured, human-readable "API Usage Report." This report will map each external library to the specific parts of its API that are used by the CatVTON codebase.
*   **Example Report Format:**
    ```markdown
    ### API Usage Report for Vendored Dependencies:

    -   **torch:**
        -   `torch.no_grad`: Used in `pipeline.py`
        -   `torch.Tensor`: Used in `utils.py`, `pipeline.py`
        -   `torch.nn.functional.interpolate`: Used in `pipeline.py`

    -   **Pillow (PIL):**
        -   `Image`: Used in `pipeline.py`, `utils.py`
        -   `ImageOps`: Used in `main.py`

    -   **fvcore.common.config:**
        -   `CfgNode`: Used in `densepose/config.py`
    ```
*   **Outcome:** A detailed and comprehensive map of the project's dependency surface area at the API level.

---

### **Phase 3: Cross-Reference and Verification (Estimated Time: 5 minutes)**

*   **Action:** I will take the detailed API Usage Report from Phase 2 and cross-reference it with the project's original `CatVTON/requirements.txt` file.
*   **Goal:** To create a "safe list" of libraries and their exact versions that are known to work with the vendored code. For each library, we will have a precise list of the API functions/classes we depend on.
*   **Outcome:** A high-confidence list of dependencies that must be pinned to their original, verified versions to guarantee stability.

---

### **Phase 4: Propose the Targeted Upgrade with Confidence**

*   **Action:** With the verified "safe list" in hand, I will propose a new, clean `requirements.txt` file.
*   **The Justification:** The proposal will be backed by the data gathered in the previous phases. Instead of a speculative upgrade, the justification will be precise:
    > "We will upgrade `diffusers`, `transformers`, `accelerate`, and `huggingface_hub` to their latest versions to resolve the `.safetensors` loading issue. The audit confirms that all other dependencies (e.g., `fvcore`, `pycocotools`, `opencv-python`) are only used for specific functions and classes with stable APIs. Therefore, we can confidently pin them to their original versions, ensuring that the complex vendored code in `detectron2` and `densepose` will not break."
*   **Outcome:** A safe, minimal, and fully justified `requirements.txt` file that solves the target problem while minimizing risk.
