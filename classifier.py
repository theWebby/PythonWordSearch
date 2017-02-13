import numpy as np
import scipy.linalg


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
            features = range(train.shape[1])

        train = train[:, features]
        test = test[:, features]

        x = np.dot(test, train.transpose())
        modtest = np.sqrt(np.sum(test * test, axis=1))
        modtrain = np.sqrt(np.sum(train * train, axis=1))
        dist = x / np.outer(modtest, modtrain.transpose())  # cosine distance
        nearest = np.argmax(dist, axis=1)
        labels = train_labels[nearest]

        return labels

    def learnPCA(data, N):
        """Performs PCA dimensionality reduction of 'data' reducing down to
        N dimensions.

        returns: (x, v)
        x - dimensionally reduced data
        v - the PCA axes (which may be useful)
        """
        ndata = data.shape[0]

        # Calculate and display the mean face
        mean_vector = np.mean(data, axis=0)

        # Calculate the mean normalised data
        deltadata = data - mean_vector

        # (You'd expect the next line to be deltadata'*deltadata but
        # a computational shortcut is being employed...)
        u = np.dot(deltadata, deltadata.transpose())
        d, pc = scipy.linalg.eigh(u, eigvals=(ndata - N, ndata - 1))
        pc = np.fliplr(pc)

        pca_axes = np.dot(pc.transpose(), deltadata)

        # compute the mean vector
        mean_vector = np.mean(data, axis=0)

        return pca_axes, mean_vector

    def reducePCA(data, pca_axes, mean_vector):
        "Performs PCA dimensionality reduction"
        # subtract mean from all data points
        centered = data - mean_vector

        # project points onto PCA axes
        reduced_data = np.dot(centered, pca_axes.transpose())

        return reduced_data
