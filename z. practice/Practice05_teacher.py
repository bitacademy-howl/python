s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.replace(',', '').replace('.', '').upper()
words = s.split(' ')
words = list(set(words))

for word in words:
    print('{0}:{1}'.format(word, s.count(word)))