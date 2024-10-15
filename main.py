# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the to keep only movies released in the 1990s 
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]
movies_1990s = subset[(subset["release_year"] < 2000)]

print("Movies released in the 90s:" + str(movies_1990s))
print("Number of movies released in the 90s:", len(movies_1990s))

# Visualize the duration column of filtered data to see the distribution of movies durations
plt.hist(movies_1990s["duration"])
plt.title("Distribution of Movie Duration in the 1990s")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()

duration = 100

# Filter data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s

# Start the counter
short_movies_count = 0

for label, row in action_movies_1990s.iterrows():
    if row["duration"] < 90:
        short_movies_count = short_movies_count + 1
    else:
        short_movies_count = short_movies_count
print("Short Movies: " + str(short_movies_count))