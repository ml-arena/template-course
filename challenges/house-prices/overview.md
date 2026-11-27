# Price RMSE — predict house prices

Estimate the sale price of **40 houses** (`h000` to `h039`). You submit your
predictions once, as a CSV; the platform scores them against the true sale
prices.

## Submission format

One file, `submission.csv`, comma-separated, with a header and exactly one row per
house:

```csv
house_id,price
h000,225.5
h001,161.5
h002,358.0
```

- `house_id` — every id from `h000` to `h039`, each once.
- `price` — your estimate, in thousands of euros; a number, never empty.

A file with other columns or missing ids is refused at upload, before any run. A
non-numeric price is caught at scoring time: the deploy fails and tells you which
house.

## Metric

Root mean squared error over the 40 houses:

$$
\mathrm{RMSE} = \sqrt{\frac{1}{40}\sum_{i=1}^{40} \left(\hat{p}_i - p_i\right)^2}
$$

**Lower is better**: the leaderboard puts the smallest RMSE first. Predicting the
mean price for every house lands around 110; a reasonable model is under 10.

## Data

`sample_submission.csv`, in the challenge's data, is a valid submission: start
from it.
