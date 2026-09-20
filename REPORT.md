# CodeAlpha Data Analytics Internship — Task 3 Report

## Task 3 — Data Visualization

### Objective

The objective of this task is to transform structured population data into meaningful visualizations and communicate important patterns through charts.

### Dataset

The dataset used for this task is `country_population.csv`.

The population data was collected from a publicly available Wikipedia webpage during Task 1 and is reused for visualization in Task 3.

### Source

Wikipedia — List of countries and dependencies by population

https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

### Tools Used

- Python
- Pandas
- Matplotlib

### Data Preparation

The population column was cleaned and converted into numeric format before creating the visualizations.

The `World` aggregate was excluded from country/location comparisons so that the charts focus on individual locations.

### Visualizations Created

Three visualizations were created:

#### 1. Top 10 Most Populated Locations

A horizontal bar chart was created to compare the populations of the 10 most populated locations in the dataset.

Output:

`outputs/top10_population_visualization.png`

#### 2. Population Share of Top 8 Locations

A pie chart was created to show the population share of the eight most populated locations.

Output:

`outputs/population_share_pie.png`

#### 3. Population Distribution

A histogram was created to show how population values are distributed across locations.

Output:

`outputs/population_distribution_visualization.png`

### Key Observation

Population values vary substantially across locations. A small number of locations have much larger populations than most other locations in the dataset.

### Output Files

The following files were generated:

- `top10_population_visualization.png`
- `population_share_pie.png`
- `population_distribution_visualization.png`
- `visualization_summary.txt`

### Conclusion

This task demonstrates how Python, Pandas, and Matplotlib can be used to transform structured population data into clear and meaningful visualizations.

The charts help communicate population comparisons, population shares, and the overall distribution of population values across locations.
