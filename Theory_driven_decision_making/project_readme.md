# Experimental Data Analysis Project

## Overview
This project involves four main R Markdown files for data analysis:
1. `Experiments_analysis.Rmd`: Analyzes experimental survey results
2. `Plato_Analysis.Rmd`: Conducts shock analysis and statistical modeling
3. `Socrates_Th1.Rmd`: Game records analysis with advanced statistical techniques
4. `Socrates_Th2.Rmd`: Further analysis of game data, focusing on time metrics and binary outcomes.

## Prerequisites
- R
- Required R Packages:
  - tidyverse
  - readr
  - dplyr
  - lubridate
  - jsonlite
  - stringr
  - psych
  - ggcorrplot
  - openxlsx
  - stringi
  - rpart
  - rpart.plot

## Data Sources
- `Finished_Survey_Results.csv`: Survey response data
- `141124_Data_Analysis.csv`: Shock analysis data
- `141124_Data_Analysis_Theories.csv`: Theoretical data for analysis
- `game_records.csv`: Game play data
- `games_headers.csv`: Game header information

## Experiments Analysis (`Experiments_analysis.Rmd`)
### Key Features
- Data cleaning and preprocessing
- Mapping of categorical variables
- Balance plot generation
- Treatment group identification
- Date and time formatting

### Main Analyses
- Demographic distribution visualization
- Treatment effect analysis
- Data transformation for statistical modeling

## Shock Analysis (`Plato_Analysis.Rmd`)
### Key Features
- Exploratory Data Analysis (EDA)
- Missing value detection
- Correlation matrix generation
- Visualization of:
  - Group distributions
  - Variable differences
  - Algorithmic aversion/liking
  - GPT usage and familiarity
  - Confidence levels

### Statistical Modeling
- Linear regression models
- Interaction effect analysis

## Game Records Analysis (`Socrates_Th1.Rmd`)
### Key Features
- Game performance analysis
- Time complexity studies
- Connection and attribute tracking
- Experimental outcome prediction

### Advanced Analyses
- Density plots of game variables
- Correlation heatmaps
- Classification trees
- Experiments correlation analysis
- Time and performance relationship exploration

### Key Visualizations
- Density plots for:
  - Total connections
  - Attributes and links
  - Play time
- Scatter plots of attributes vs. expected probability
- Correlation heatmaps
- Classification decision trees

## Advanced Game Analysis (`Socrates_Th2.Rmd`)
### Key Features
- Handling noisy data through preprocessing
- Time-based metrics calculation:
  - Start and finish times
  - Total time required
- Filtering empty or invalid data
- Classification of results into binary outcomes

### Main Analyses
- Mean time calculation for specific game subsets
- Removal of outliers and invalid theories
- Exploration of time distributions and their impact on outcomes
- Binary classification for result prediction

### Key Visualizations
- Histograms and density plots of time-based metrics
- Boxplots for comparison of groups with and without valid theories
- Scatter plots of game variables and outcomes

## How to Run
1. Install required R packages
2. Set working directory to project folder
3. Open and run each Rmd file in RStudio

## Visualizations
The scripts generate multiple visualizations including:
- Bar plots for demographic distribution
- Boxplots for group comparisons
- Correlation heatmaps
- Density plots
- Scatter plots
- Decision trees

## Author
Giacomo Negri

## Notes
- Ensure data files are in the correct directory
- Some file paths may need local adjustment
- Recommended to review and potentially modify data cleaning steps

## Potential Improvements
- Add more robust error handling
- Implement additional statistical tests
- Create more interactive visualizations
- Expand predictive modeling techniques
