import matplotlib.pyplot as plt

# %%
def generate_bar_char():
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    
    plt.show()

# %%
if __name__ == '__main__':
    generate_bar_char()