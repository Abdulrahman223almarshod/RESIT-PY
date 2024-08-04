

import csv
import statistics

def html_stats(csv_file, html_file, title:str = None) -> None:
    # Check if the CSV file exists
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found!")

    # Compute statistics for each column
    columns = reader.fieldnames
    stats = {column: {"min": None, "max": None, "mean": None, "median": None} for column in columns}
    
    for column in columns:
        try:
            values = [float(row[column]) for row in data if row[column].isdigit()]
            stats[column]["min"] = min(values)
            stats[column]["max"] = max(values)
            stats[column]["mean"] = statistics.mean(values)
            stats[column]["median"] = statistics.median(values)
        except ValueError:
            continue
    
    # Generate HTML content
    if title is None:
        title = f"Column statistics for {csv_file}"
    
    html_content = f"<html><head><title>{title}</title></head><body>"
    html_content += f"<h1>{title}</h1>"
    html_content += "<table border='1' style='background-color: #f2f2f2;'>"
    html_content += "<tr><th>Column</th><th>Min</th><th>Max</th><th>Mean</th><th>Median</th></tr>"
    
    row_counter = 0
    for column, stat in stats.items():
        row_style = ""
        if row_counter == 0:
            row_style = " style='background-color: #add8e6;'"  # Light blue
        elif row_counter == 2:
            row_style = " style='background-color: #90ee90;'"  # Light green
        
        html_content += f"<tr{row_style}><td>{column}</td><td>{stat['min']}</td><td>{stat['max']}</td><td>{stat['mean']}</td><td>{stat['median']}</td></tr>"
        row_counter += 1
    
    html_content += "</table></body></html>"
    
    # Write HTML content to file
    with open(html_file, 'w') as file:
        file.write(html_content)

# Example usage
if __name__ == "__main__":
    html_stats("data.csv", "statistics.html", "Column statistics for data.csv")

