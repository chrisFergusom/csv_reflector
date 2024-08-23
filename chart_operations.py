# chart_operations.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from utilities import get_category

def generate_pie_chart(data, title, ax):
    counts = data.value_counts()
    ax.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)

def generate_line_chart(df, ax):
    # Convert index to datetime and extract date and hour
    df['DateTime'] = pd.to_datetime(df.index)
    df['Date'] = df['DateTime'].dt.date
    df['Hour'] = df['DateTime'].dt.hour

    # Aggregate data by date and hour
    hourly_data = df.groupby(['Date', 'Hour', 'Button']).size().unstack(fill_value=0)
    
    # Flatten the multi-index
    hourly_data.index = pd.to_datetime(hourly_data.index.get_level_values('Date')) + pd.to_timedelta(hourly_data.index.get_level_values('Hour'), unit='h')
    hourly_data = hourly_data.sort_index()

    # Calculate total presses per hour
    hourly_total = hourly_data.sum(axis=1)
    
    # Resample to ensure all hours are present
    date_range = pd.date_range(start=hourly_total.index.min(), end=hourly_total.index.max(), freq='H')
    hourly_total = hourly_total.reindex(date_range, fill_value=0)

    # Calculate moving average
    window_size = 24  # 24 hours for daily average
    hourly_avg = hourly_total.rolling(window=window_size, center=True).mean()

    # Custom color scheme
    colors = plt.cm.Set3(np.linspace(0, 1, len(hourly_data.columns)))
    
    # Plot individual button presses
    for i, button in enumerate(hourly_data.columns):
        ax.plot(hourly_data.index, hourly_data[button], label=button, color=colors[i], alpha=0.7)

    # Plot average line
    ax.plot(hourly_avg.index, hourly_avg.values, label='Hourly Average', color='red', linewidth=2)

    # Set x-axis limits and format
    ax.set_xlim(hourly_total.index.min(), hourly_total.index.max())
    
    # Update x-axis ticks and labels
    hours = mdates.HourLocator(interval=6)  # Show tick every 6 hours
    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n%H:%M'))
    
    ax.set_title('Button Press Frequency Over Time')
    ax.set_xlabel('')
    ax.set_ylabel('Number of Presses')
    plt.xticks(rotation=45, ha='right')
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

def show_charts(df, gui):
    df['Category'] = df['Button'].map(lambda x: get_category(x, gui.button_categories))
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 6))
    
    # Button Usage Pie Chart
    generate_pie_chart(df['Button'], 'Button Usage', ax1)

    # Category Usage Pie Chart
    generate_pie_chart(df['Category'], 'Category Usage', ax2)

    # Button Press Frequency Over Time
    generate_line_chart(df, ax3)
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()