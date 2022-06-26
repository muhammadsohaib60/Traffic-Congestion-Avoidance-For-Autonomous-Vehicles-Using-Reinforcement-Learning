"""import random
from collections import namedtuple

# Taken from
# https://github.com/pytorch/tutorials/blob/master/Reinforcement%20(Q-)Learning%20with%20PyTorch.ipynb

Transition = namedtuple('Transition', ('state', 'action', 'mask', 'next_state',
                                       'reward'))


class Memory(object):
    def __init__(self):
        self.memory = []

    def push(self, *args):
       # Saves a transition.
        self.memory.append(Transition(*args))

    def sample(self):
        return Transition(*zip(*self.memory))

    def __len__(self):
        return len(self.memory) """
import random
#The **Memory** class handle the memorization for the experience replay mechanism. A function is used to add a sample into the memory, while the other function retrieves a batch of samples from the memory.
# HANDLES THE MEMORY
class Memory:
    def __init__(self, memory_size):
        self._memory_size = memory_size
        self._samples = []

    # ADD A SAMPLE INTO THE MEMORY
    def add_sample(self, sample):
        self._samples.append(sample)
        if len(self._samples) > self._memory_size:
            self._samples.pop(0)  # if the length is greater than the size of memory, remove the oldest element

    # GET n_samples SAMPLES RANDOMLY FROM THE MEMORY
    def get_samples(self, n_samples):
        if n_samples > len(self._samples):
            return random.sample(self._samples, len(self._samples))  # get all the samples
        else:
            return random.sample(self._samples, n_samples)  # get "batch size" number of samples

