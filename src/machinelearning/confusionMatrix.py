import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score


actual = np.random.binomial(1,.9, size =1000)
prediction = np.random.binomial(1,.9, size =1000)

confMatrix = metrics.confusion_matrix(actual, prediction)

accuracy = metrics.accuracy_score(actual, prediction)

precision = metrics.precision_score(actual, prediction)

print("Accuracy is: ",accuracy)
print("Precision is: ",precision)

display = metrics.ConfusionMatrixDisplay(confusion_matrix=confMatrix, display_labels=[0,1])



display.plot()
plt.show()