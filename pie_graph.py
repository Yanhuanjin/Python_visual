import matplotlib.pyplot as plt

while True:
    values = list(input('Please input the values:').split())
    labels = list(input('Please input the labels:').split())
    if len(values) != len(labels):
        print('You values does not equal to your labels, please restart')
    else:
        break
colors_list = ['y','g','r','c','m','b']
colors = colors_list[:len(labels)]
plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%',
        counterclock=False, shadow=False)
plt.title('Values')

plt.show()
