import matplotlib.pyplot as plt

Title = input("Please input the title: ")
while True:
    values = list(input('Please input the values: ').split())
    labels = list(input('Please input the labels: ').split())
    if len(values) != len(labels):
        print('You values does not equal to your labels, please restart')
    else:
        break
colors_list = ['r','g','y','b','m','c']
colors = colors_list[:len(labels)]
plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%',
        counterclock=False, shadow=False)
plt.title(Title)

plt.show()
