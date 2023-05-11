from matplotlib import pyplot as plt

def mat(data):

#    sizes = [10, 100, 1000, 5000, 10000, 20000, 50000]
   sizes = [10, 100, 1000]
   types = ["random", "best", "worst"]
   colors = ['blue', 'green', 'red']

   fig, axs = plt.subplots(ncols=2, figsize=(10, 5))
   fig.suptitle('Time complexity comparison')
   fig.tight_layout()


   axs[0].set(title="Simple quick sort", ylabel='Operations', xlabel='Array size')
   axs[0].grid()
   axs[1].set(title="Quick sort with 3d median", ylabel='Operations', xlabel='Array size')
   axs[1].grid()

#    x_cords = range(0, 50000)
#    y_cords = [x*x for x in x_cords]
#    y_cords2 = [x for x in x_cords]

   i = 0
   for type in types:
      py_dev_y = data[type]['quick_sort'].values()
      axs[0].plot(sizes, py_dev_y, marker="o", label=type, color=colors[i])
      i += 1

#    axs[0].plot(x_cords, y_cords, color="purple", linestyle='--', label="O(n^2)")
      
   i = 0
   for type in types:
      py_dev_y = data[type]['quick_median'].values()
      axs[1].plot(sizes, py_dev_y, marker="o", label=type, color=colors[i])
      i += 1
#    axs[1].plot(x_cords, y_cords, color="purple", linestyle='--', label="O(n^2)")
#    axs[1].plot(x_cords, y_cords2, color="yellow", linestyle='--', label="O(n)")

   axs[0].legend()
   axs[1].legend()

   plt.show()