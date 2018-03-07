from neuron import Neuron
import numpy as np

class GSOM:
    def __init__(self, initial_map_size, parent_quantization_error, t1, t2, growing_metric, weights_vectors_dict=None):
        self.__t1 = t1
        self.__t2 = t2
        self.__parent_quantization_error = parent_quantization_error
        self.__map_size = initial_map_size

        # i'm not so sure...
        self.neurons_map = np.asarray(
            a=[[None for _ in range(initial_map_size[0])] for _ in range(initial_map_size[1])],
            dtype=object
        )
        if weights_vectors_dict is not None:
            for position, weight in weights_vectors_dict.items():
                self.neurons_map[position] = Neuron(weight, self.__parent_quantization_error, self.__t2, growing_metric)

    def winner_idx(self, data):
        activations = np.empty(shape=self.neurons_map.shape, dtype=np.float32)

        activations_iter = np.nditer(activations, flags=['multi_index'])
        while not activations_iter.finished:
            activations[activations_iter.multi_index] = self.neurons_map[activations_iter.multi_index](data)
            activations_iter.iternext()

        return np.unravel_index(activations.min(), dims=activations.shape)

    def train(self, input_dataset, epochs, learning_rate, decay, gaussian_sigma):
        raise NotImplementedError

    def __can_grow(self, input_dataset):
        MQE = 0.0
        mapped_neurons = 0

        self.__map_data_to_unit(input_dataset)
        neuron_iter = np.nditer(self.neurons_map, flags=['multi_index'])
        while not neuron_iter.finished:
            neuron = self.neurons_map[neuron_iter.multi_index]
            if len(neuron.input_dataset) != 0:
                MQE += neuron.compute_quantization_error()
                mapped_neurons += 1
            neuron_iter.iternext()

        return (MQE / mapped_neurons) >= (self.__t1 * self.__parent_quantization_error)

    def __map_data_to_unit(self, input_dataset):
        # reset previous mapping
        neuron_iter = np.nditer(self.neurons_map, flags=['multi_index'])
        while not neuron_iter.finished:
            self.neurons_map[neuron_iter.multi_index].input_dataset.clear()
            neuron_iter.iternext()
        # finding the new association for each neuron
        for data in input_dataset:
            winner = self.winner_idx(data)
            self.neurons_map[winner].input_dataset.append(data)

    def find_error_unit(self):
        raise NotImplementedError

    def find_most_dissimilar_unit(self, error_unit):
        raise NotImplementedError

    def grow(self):
        raise NotImplementedError

    def expand_column(self, error_unit_column_idx, dissimilar_unit_column_idx):
        raise NotImplementedError

    def expand_row(self, error_unit_row_idx, dissimilar_unit_row_idx):
        raise NotImplementedError

    def adjacent_units_direction(self, unit1, unit2):
        # returns horizontal or vertical
        raise NotImplementedError

    def init_new_unit_weight_vector(self, unit_idx):
        # the new units weight vector are initialized
        # as the average of their corresponding neighbors.
        raise NotImplementedError
