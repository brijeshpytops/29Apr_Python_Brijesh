# import math

# print(dir(math))

# print(math.sin(90))
# print(math.factorial(5))
# print(math.sqrt(4))
# print(math.sqrt(16))

import random

# print(random.randint(1, 100))
# print(random.randrange(1, 100, 2))

musics = ['music-1.mp3','music-2.mp3','music-3.mp3','music-4.mp3','music-5.mp3']

# random.shuffle(musics)

# print(musics)


from datetime import datetime, timedelta

# current_datetime = datetime.now().date()
# current_datetime = datetime.now().time()
# current_datetime = datetime.now().day
# current_datetime = datetime.now().month
# current_datetime = datetime.now().weekday()

# current_datetime = datetime.now()

# f_time = current_datetime + timedelta(days=1, hours=1.5)

# print(f_time)

# import time
# 
# ques = []
# for num in range(1, 11):
#     ques.append(f'Q-{num}')
# 
# start = 1
# end = len(ques)
# while(start <= end):
#     print(ques[start-1])
#     time.sleep(5)
#     start+=1

import os
import uuid
import time

# # print(os.system('mkdir test'))
# print(os.system('type nul > test.txt'))
# 
# while(1):
#     os.system(f'type nul > {uuid.uuid4()}_.pdf')
#     time.sleep(5)
#    


import matplotlib.pyplot as plt
from fpdf import FPDF

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Plotting the data
plt.figure()
plt.plot(x, y, marker='o')
plt.title('Sample Data Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Save the plot to an image file
plot_filename = 'plot.png'
plt.savefig(plot_filename)
plt.close()

# Create a PDF and add the plot image
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Sample Data Plot')
pdf.image(plot_filename, x=10, y=20, w=180)  # Adjust x, y, w as needed

# Save the PDF
pdf_filename = 'plot.pdf'
pdf.output(pdf_filename)

print(f'Plot saved as {plot_filename}')
print(f'PDF saved as {pdf_filename}')
