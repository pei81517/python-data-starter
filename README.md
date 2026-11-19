# Python Data Science Starter

A collection of Python scripts exploring data analysis, loops, and probability simulations.

## Projects
- **dice_chart.py**: Simulates 10,000 rolls of two six-sided dice and visualizes the normal probability distribution of sums (2–12) using a terminal bar chart.
- **line_finder.py**: Interactive IGCSE math tool that calculates the gradient ($m$), y-intercept ($c$), and linear equation ($y = mx + c$) from any two coordinate points.
- **grade_analyzer.py**: Reads student exam data from `scores.csv`, calculates subject averages, and identifies the top performer.
- **pi_estimator.py**: Uses a Monte Carlo random dart simulation and coordinate geometry ($x^2 + y^2 \le 1$) to approximate $\pi$ and measure margin of error.
- **pie_visual.py**: Renders a live 2D geometric animation using Python `turtle` to visualize Monte Carlo dart throws inside and outside an inscribed circle.
- **climate_analyzer.py**: Compares 12-month climate datasets (`climate_data.csv`) between Auckland and Shenzhen to calculate annual averages, seasonal swings, and hemispheric temperature gaps.
- **climate_chart.py**: Plots a dual time-series line graph comparing 12 months of Auckland and Shenzhen temperatures from `climate_data.csv` using Python `turtle`.
- **trend_predictor.py**: Implements Ordinary Least Squares linear regression ($y = mx + c$) and Pearson correlation ($r$) from scratch to predict exam scores from study hours.
- **regression_plot.py**: Renders a visual scatter plot, Least Squares line of best fit ($y = mx + c$), and predicted outcome point using Python `turtle`.
- **aukland_vs_shenzhen.py**: Analyzes 12-month climate data with `pandas` and generates a high-resolution comparison chart using `matplotlib`.
- **monty_hall.py**: Simulates 10,000 rounds of the Monty Hall game show problem to prove mathematically why switching doors wins ~66.7% of the time vs. ~33.3% when staying.
### Featured Visualization: Auckland vs. Shenzhen Temperature
![Auckland vs Shenzhen Temperature](auckland_vs_shenzhen.png)

### Featured Visualization: Monty Hall Simulation

![Monty Hall Simulation Results](monty_hall_results.png)
## Men's 100m World Record Progression (1912–2009)
Using `pandas` and `scikit-learn`, this project analyzes ratified electronic/official Men's 100m world records and fits a linear regression trendline to project future performance.

* **Key Findings:** Record times dropped from 10.60s (1912) to Usain Bolt's 9.58s (2009), reaching an average speed of 10.44 m/s. While a straight-line trend projects 9.54s by 2028, real human sprinting speed approaches a biological limit.
* **Notebook:** [`100m_world_record_analysis_ipynb_.ipynb`](./100m_world_record_analysis_ipynb_.ipynb)
![Men's 100m World Record Progression](./100m_progression.png)
