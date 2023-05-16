from abc import ABC, abstractmethod

class BaseFrequencyCounter(ABC):
    def __init__(self, filePath):
        self.filePath = filePath

    @abstractmethod
    def computeFrequencies(self):
        pass


class ListFrequencyCounter(BaseFrequencyCounter):
    def computeFrequencies(self):
        with open(self.filePath, 'r') as fileObject:
            content = fileObject.read().lower()

        charList = [char for char in content if char.isalpha()]

        distinctChars = list(set(charList))
        frequencyData = []

        for char in distinctChars:
            frequencyData.append(f"{char} = {charList.count(char)}")

        for item in frequencyData:
            print(item)


class DictFrequencyCounter(BaseFrequencyCounter):
    def computeFrequencies(self):
        with open(self.filePath, 'r') as fileObject:
            content = fileObject.read().lower()

        charDict = {char: 0 for char in content if char.isalpha()}

        for char in content:
            if char in charDict:
                charDict[char] += 1

        for key, value in charDict.items():
            print(f'"{key}" {value}')



listFreqCounter = ListFrequencyCounter('weirdWords.txt')
listFreqCounter.computeFrequencies()

print("\n-------------------\n")


dictFreqCounter = DictFrequencyCounter('weirdWords.txt')
dictFreqCounter.computeFrequencies()
