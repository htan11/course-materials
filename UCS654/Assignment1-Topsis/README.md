# Topsis-Harsh-102303812

A Python package to implement **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) for multi-criteria decision analysis.

**Author:** Harsh Tanwar  
**Roll No:** 102303812  
**Email:** htanwar_be23@thapar.edu  

**Repository:** [Assignment1-Topsis](https://github.com/htan11/course-materials/tree/main/UCS654/Assignment1-Topsis)

---

## What is TOPSIS?

TOPSIS ranks alternatives by comparing each to an *ideal positive* and *ideal negative* solution. Alternatives closer to the ideal positive and farther from the ideal negative get higher scores and better ranks. The method uses vector normalization, weighted criteria, and Euclidean distances to compute a performance score for each alternative.

---

## Requirements

- Python 3.6+
- **pandas** – data handling
- **numpy** – numerical operations

Install dependencies:

```bash
pip install pandas numpy
```

---

## Installation

### From PyPI (if published)

```bash
pip install Topsis-Harsh-102303812
```

### From source (clone or download the repo)

```bash
git clone https://github.com/htan11/course-materials.git
cd course-materials/UCS654/Assignment1-Topsis
pip install .
```

Or, in the folder containing `setup.py`:

```bash
pip install .
```

---

## Usage

### Command line

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

**Example (with 5 criteria):**

```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,-" result.csv
```

### As a Python module

```python
from Topsis_Harsh_102303812.topsis import topsis

topsis("data.csv", "1,1,1,1,1", "+,+,-,+,-", "result.csv")
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| **InputDataFile** | Path to a CSV file: first column = alternative names, remaining columns = numeric criterion values. Must have a header row. |
| **Weights** | Comma-separated weights for each criterion (e.g. `"1,1,1,2,1"`). Number of values must match number of criteria. |
| **Impacts** | Comma-separated impacts: `+` for beneficial (higher is better), `-` for non-beneficial (lower is better). Same count as criteria. |
| **OutputResultFileName** | Path for the output CSV. Contains original columns plus **Topsis Score** and **Rank**. |

- Beneficial (`+`): e.g. Quality, Customer Rating — higher value is better.  
- Non-beneficial (`-`): e.g. Price, Delivery Time — lower value is better.

---

## Input file format

CSV with a header; first column = alternative names, rest = numeric only.

**Example (`data.csv`):**

| Product | Quality | Price | Features | Customer Rating | Delivery Time |
|---------|---------|-------|----------|-----------------|---------------|
| A1      | 8.5     | 450   | 7.2      | 4.3             | 3             |
| A2      | 7.8     | 380   | 8.1      | 4.5             | 5             |
| ...     | ...     | ...   | ...      | ...             | ...           |

- Column 1: labels (not used in math).  
- Columns 2–6: criteria. Weights and impacts must be given for each of these in order.

---

## Example with this dataset

For 5 criteria (Quality, Price, Features, Customer Rating, Delivery Time):

- **Weights:** `"1,1,1,1,1"` (equal weight).  
- **Impacts:** `"+,+,-,+,-"` (Quality +, Price +, Features -, Customer Rating +, Delivery Time -).

Run:

```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,-" result.csv
```

Output CSV will have all input columns plus:

- **Topsis Score** – higher is better.  
- **Rank** – 1 = best alternative.

---

## Output

The result file contains:

- All original columns.  
- **Topsis Score** – performance score in [0, 1].  
- **Rank** – integer rank (1 = best).

Example message: `Result file 'result.csv' created successfully.`

---

## Project structure

```
assignment1_DS-main/
├── README.md
├── setup.py
├── data.csv              # Sample input
├── Topsis_Harsh_102303812/
│   ├── __init__.py
│   └── topsis.py         # TOPSIS implementation
└── LICENSE
```
## Link
https://colab.research.google.com/drive/1hFhuzNVxJ53LJTjMrJsID8C_r-0W3Nya?usp=sharing

---

## License

MIT License. See [LICENSE](LICENSE) for details.
