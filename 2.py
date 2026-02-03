import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt

# 1. Prepare data (manually provided fertility rate data)
data = {
    'observation_date': [
        '1960-01-01', '1961-01-01', '1962-01-01', '1963-01-01', '1964-01-01',
        '1965-01-01', '1966-01-01', '1967-01-01', '1968-01-01', '1969-01-01',
        '1970-01-01', '1971-01-01', '1972-01-01', '1973-01-01', '1974-01-01',
        '1975-01-01', '1976-01-01', '1977-01-01', '1978-01-01', '1979-01-01',
        '1980-01-01', '1981-01-01', '1982-01-01', '1983-01-01', '1984-01-01',
        '1985-01-01', '1986-01-01', '1987-01-01', '1988-01-01', '1989-01-01',
        '1990-01-01', '1991-01-01', '1992-01-01', '1993-01-01', '1994-01-01',
        '1995-01-01', '1996-01-01', '1997-01-01', '1998-01-01', '1999-01-01',
        '2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01', '2004-01-01',
        '2005-01-01', '2006-01-01', '2007-01-01', '2008-01-01', '2009-01-01',
        '2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01',
        '2015-01-01', '2016-01-01', '2017-01-01', '2018-01-01', '2019-01-01',
        '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01'
    ],
    'fertility_rate': [
        3.654, 3.62, 3.461, 3.319, 3.19, 2.913, 2.721, 2.558, 2.464, 2.456,
        2.48, 2.266, 2.01, 1.879, 1.835, 1.774, 1.738, 1.79, 1.76, 1.808,
        1.8395, 1.812, 1.8275, 1.799, 1.8065, 1.844, 1.8375, 1.872, 1.934, 2.014,
        2.081, 2.0625, 2.046, 2.0195, 2.0015, 1.978, 1.976, 1.971, 1.999, 2.0075,
        2.056, 2.0305, 2.0205, 2.0475, 2.0515, 2.057, 2.108, 2.12, 2.072, 2.002,
        1.931, 1.8945, 1.8805, 1.8575, 1.8625, 1.8435, 1.8205, 1.7655, 1.7295, 1.706,
        1.6415, 1.664, 1.6565, 1.6165
    ]
}

# 2. Create DataFrame and convert date column
df = pd.DataFrame(data)
df['observation_date'] = pd.to_datetime(df['observation_date'])
df.set_index('observation_date', inplace=True)

# 3. Plot fertility rate trend
plt.figure(figsize=(14, 8))
plt.plot(
    df.index,
    df['fertility_rate'],
    marker='o',
    linewidth=2,
    markersize=4,
    label='Total Fertility Rate (United States)'
)

# 4. Add key points and reference line
max_rate = df['fertility_rate'].max()
min_rate = df['fertility_rate'].min()
max_year = df['fertility_rate'].idxmax().year
min_year = df['fertility_rate'].idxmin().year

plt.scatter(df['fertility_rate'].idxmax(), max_rate, s=100, zorder=5)
plt.scatter(df['fertility_rate'].idxmin(), min_rate, s=100, zorder=5)

# Replacement-level fertility reference line (2.1)
plt.axhline(
    y=2.1,
    linestyle='--',
    linewidth=1.5,
    alpha=0.7,
    label='Replacement-Level Fertility (2.1)'
)

# 5. Chart styling
plt.title(
    'Total Fertility Rate in the United States (1960–2023)',
    fontsize=16,
    fontweight='bold',
    pad=20
)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Births per Woman', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(fontsize=11)

# Annotate key values
plt.annotate(
    f'Peak: {max_rate:.2f} ({max_year})',
    xy=(df['fertility_rate'].idxmax(), max_rate),
    xytext=(10, 15),
    textcoords='offset points',
    fontsize=10
)

plt.annotate(
    f'Lowest: {min_rate:.3f} ({min_year})',
    xy=(df['fertility_rate'].idxmin(), min_rate),
    xytext=(10, -25),
    textcoords='offset points',
    fontsize=10
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("us_total_fertility_rate_1960_2023.png")
# 6. Display the plot
plt.show()

# 7. Print key statistics
print("=== Key Statistics: U.S. Total Fertility Rate ===")
print(f"Time range: {df.index.year.min()} – {df.index.year.max()}")
print(f"Historical peak: {max_rate:.3f} ({max_year})")
print(f"Historical low: {min_rate:.3f} ({min_year})")
print(f"Latest value (2023): {df['fertility_rate'].iloc[-1]:.3f}")
print(
    f"Change from 1960 to 2023: "
    f"{df['fertility_rate'].iloc[-1] - df['fertility_rate'].iloc[0]:.3f}"
)
print(
    f"Below replacement level (2.1): "
    f"{'Yes' if df['fertility_rate'].iloc[-1] < 2.1 else 'No'}"
)