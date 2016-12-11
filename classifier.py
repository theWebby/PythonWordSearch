import numpy as np


class Classifier:
    """
    Methods that have been supplied to help complete the assignment
    """

    @staticmethod
    def classify(train, train_labels, test, features=None):
        """Nearest neighbour classification

        train - matrix of training data (one sample per row)
        train_labels - corresponding training data labels
        test - matrix of samples to classify

        returns: labels - vector of test data labels
        """

        if features is None:
            features = np.arange(0, train.shape[1])

        train = train[:, features]
        test = test[:, features]

        x = np.dot(test, train.transpose())
        modtest = np.sqrt(np.sum(test * test, axis=1))
        modtrain = np.sqrt(np.sum(train * train, axis=1))
        dist = x / np.outer(modtest, modtrain.transpose())  # cosine distance
        nearest = np.argmax(dist, axis=1)
        labels = train_labels[nearest]

        return labels


