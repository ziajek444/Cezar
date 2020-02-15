import time
import random
from keygen_supercezar import _generate_unique_list

# performance test for 2 implementation
# how to create public key asap

# implementation without "random.sample"
def _generate_unique_list2(amountElements=24064,rangeElements=(0,65536),seed=None):
    minval = rangeElements[0]
    maxval = rangeElements[1]
    initialList = []
    outputList = []
    if minval > maxval:
        maxval, minval = minval, maxval
    wholeElements = maxval - minval

    if wholeElements < amountElements:
        raise Exception("range is too low")

    random.seed(a=seed, version=2)
    filling = wholeElements-amountElements
    if filling-amountElements > amountElements:
        # initial list is much bigger than output will be
        initialList = [x for x in range(minval, maxval)]
        ll = len(initialList)
        for e in range(amountElements, 0, -1):
            ll -= 1
            outputList.append(initialList.pop(random.randint(0, ll)))
    else:
        outputList = [x for x in range(minval, maxval)]
        ll = len(outputList)
        for e in range(filling):
            ll -= 1
            outputList.pop(random.randint(0, ll))
        random.shuffle(outputList)

    return outputList


start = time.time()
for e in range(100):
    tmp = _generate_unique_list2(600,(60,123456))
end = time.time()
print(end - start)

start = time.time()
for e in range(100):
    tmp = _generate_unique_list(600,(60,123456))
end = time.time()
print(end - start)

# 15.02.2020: output:
# 2.459432601928711
# 0.4719233512878418
