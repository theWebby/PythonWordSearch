import numpy as np


class GivenMethods:
    """
    Methods that have been supplied to help complete the assignment
    """

    def classify(train, train_labels, test):
        """Nearest neighbour classification

        train - matrix of training data (one sample per row)
        train_labels - corresponding training data labels
        test - matrix of samples to classify

        returns: labels - vector of test data labels
        """

        x = np.dot(test, train.transpose())
        modtest = np.sqrt(np.sum(test * test, axis=1))
        modtrain = np.sqrt(np.sum(train * train, axis=1))
        dist = x / np.outer(modtest, modtrain.transpose())  # cosine distance
        nearest = np.argmax(dist, axis=1)
        labels = train_labels[nearest]

        return labels


