import plag_training
import string
import numpy
from scipy.sparse import vstack as vstack_sparse_matrices

# call function plag_training to find out tfidf and tfs for the training files
tfidf, tfs, files = plag_training.training_tfs()

# open input file
f = open("input.txt", encoding="utf-8")
files.append("input.txt")
print(f)
print("--------------------------------------------------------")
# convert input file data to lower case
text = f.read().lower().translate(string.punctuation)
print(text)
# now get tfidf for the input file and combine with the previous model
response = tfidf.transform([text])
tfs_combined = vstack_sparse_matrices([tfs, response])

# now calculate the similarity of files with each other
mat = (tfs_combined * tfs_combined.T).A

# printing out plagiarized files
no_ofRows = len(mat)

# find out percantage plagarization for input files with training files
for x in range(0, len(mat[0]) - 1):
    if (mat[no_ofRows - 1, x] > 0.5):
        print(f"Текущий фал для проверки совпадает с {files[x]} на {mat[no_ofRows - 1][x] * 100} процентов")
else:
     print(f"Нормальный процент уникальности, меньше 50%")