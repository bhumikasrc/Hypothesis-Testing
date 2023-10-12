# What Is Hypothesis Testing❓

<p align="center">
    <img src="https://editor.analyticsvidhya.com/uploads/52940cover.jpg" alt="GitHub Logo" width="400" height="300">
</p>
<p align="center">Photo by Analytics Vidhya</p>



## Definition

Hypothesis testing is a statistical method used to make informed decisions about a population based on sample data. It involves formulating two competing hypotheses, the null hypothesis (H0) and the alternative hypothesis (Ha), and then collecting and analyzing data to determine whether there is enough evidence to reject the null hypothesis in favor of the alternative hypothesis.


## Statistical Methods

• <u>T Test</u> - The t-test is a statistical hypothesis test used to determine whether:

* the sample mean is significantly different from a guess about the population mean

* there is a significant difference between the means of two groups or samples

It is particularly useful when working with small sample sizes and is employed to assess whether the observed differences in sample means are likely to represent true differences in the population or if they could have occurred by chance.

## Clone the repository

```git clone https://github.com/bhumikasrc/Hypothesis-Testing.git```

## Install packages

### Data storage and retrieval

```py
import numpy as np
import pandas as pd
```

### Visualization 

```py
import seaborn as sns
import matplotlib.pyplot as plt
```

### Statistical analysis

```py
from scipy import stats
import statsmodels.api as sm
```

### Building a Deck

```py
import streamlit as st
```

## Explore the Code demo

1. Loading the dataset
2. Formulating the hypothesis test set
3. Conducting the test using statistical test methods
4. Visualizing the distribution of the data
5. Cross check test restults using p-value (optional)

## Explore the Final Presentation

1. On site sample data collection
2. 2 Sample t-test using collected data
3. 2 Sample t-test using LR model
4. Discussing type I and type II errors in hypothesis tests
5. Using 2 generated samples to display hypothesis testing
6. P-hacking by resampling
7. P-hacking by selectively choosing data
