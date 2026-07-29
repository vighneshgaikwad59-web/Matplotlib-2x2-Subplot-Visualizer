# Matplotlib 2x2 Subplot Visualizer

A simple Python script that demonstrates how to create a **2x2 grid of subplots** using Matplotlib, showcasing different chart types (bar, line, horizontal bar) with a shared data array.

## 📊 What it does

Given a NumPy array `x = [1, 2, 3, 4, 5]`, the script plots four different transformations of `x` in a single 2x2 figure:

| Position | Chart Type | Data | Description |
|----------|-----------|------|--------------|
| Top-left | Bar chart | `x * 2` | Default color bar plot |
| Top-right | Line plot | `x * 3` | Light blue line |
| Bottom-left | Bar chart | `x * 5` | Purple bar plot |
| Bottom-right | Horizontal bar | `x * 4` | Yellow horizontal bars |

## 🛠️ Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
```

## ▶️ Usage

Run the script directly:
```bash
python subplot_visualizer.py
```

This will open a window displaying all four subplots arranged in a 2x2 grid, with `tight_layout()` applied for clean spacing.


## 📝 Notes

- `axis` is a 2D array of subplot axes, indexed as `axis[row, col]`.
- `plt.tight_layout()` automatically adjusts spacing so titles/labels don't overlap.
- This project is a good starting point for learning how to lay out multiple related plots — useful for comparing distributions or metrics side by side (e.g., in bioinformatics data exploration).

## 📌 To Do / Improvements

- Add axis labels (`set_xlabel`, `set_ylabel`) for clarity
- Save the figure to a file using `plt.savefig()`
- Parameterize the data and colors for reuse with real datasets

