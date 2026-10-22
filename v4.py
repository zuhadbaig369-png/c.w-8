import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

type = [blood_sugar_men, blood_sugar_women]
colors = ['g', 'r']
label = ['Men', 'Women']
bins = [80, 100, 125, 150]
plt.xlabel("blood sugar range")
plt.ylabel("total no. of patients")
plt.hist(type, bins=bins, rwidth=.95, color=colors, label=label, orientation="horizontal")
plt.title("blood sugar of patients")
plt.legend()
plt.show()