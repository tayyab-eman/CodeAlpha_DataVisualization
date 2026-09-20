# CodeAlpha Data Analytics Internship — Task 3: Data Visualization

## Objective

The objective of this task is to transform population data into meaningful visualizations and communicate important patterns through charts.

## Dataset

The dataset contains population information collected from a publicly available population webpage.

The dataset contains the following columns:

- Country / Location
- Population
- World Percentage
- Date
- Source

## Tools Used

- Python
- Pandas
- Matplotlib

## Visualizations Created

Three visualizations were created:

1. **Top 10 Most Populated Locations** — Bar Chart
2. **Population Share of Top 8 Locations** — Pie Chart
3. **Population Distribution Across Locations** — Histogram

The World aggregate was excluded from country/location comparisons so that the charts focus on individual locations.

## Key Observation

Population values vary substantially across locations, with a small number of locations having much larger populations than most others.

## Output Files

The visualizations and summary are stored in the `outputs` folder:

- `top10_population_visualization.png`
- `population_share_pie.png`
- `population_distribution_visualization.png`
- `visualization_summary.txt`

## Project Structure

```text
CodeAlpha_DataVisualization/
│
├── data/
│   └── country_population.csv
│
├── outputs/
│   ├── top10_population_visualization.png
│   ├── population_share_pie.png
│   ├── population_distribution_visualization.png
│   └── visualization_summary.txt
│
├── task3_visualization.py
├── README.md
├── REPORT.md
└── requirements.txt
