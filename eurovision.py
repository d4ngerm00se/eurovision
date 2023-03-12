import pandas as pd

eurovision_data = pd.read_csv("C:/Users/danaa/Downloads/Countries_Editions_Songs.csv", na_values='–')

#print(eurovision_data.head())

#print("Number of rows:", eurovision_data.shape[0])

#Cleaning out rows where no song/artist as the country did not participate
euro_data = eurovision_data.dropna(subset=['songs', 'artists'])

#print("Number of rows:", euro_data.shape[0])

#print(euro_data.info())


#got rid of any semi-finals data to be able to calculate mean placement in the finals
finale_only = euro_data.dropna(subset=['points'])

print(finale_only.head())

finale_only['places'] = finale_only['places'].replace('#1', '1')

finale_only['places'] = finale_only['places'].astype(int)

# Group the DataFrame by the "country" column and calculate the mean placement
mean_placement = finale_only.groupby('country')['places'].mean()

# Sort the resulting DataFrame by the mean placement in ascending order
mean_placement = mean_placement.sort_values(ascending=True)

# Print the resulting DataFrame
print(mean_placement)