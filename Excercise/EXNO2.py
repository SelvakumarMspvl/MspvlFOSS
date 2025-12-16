import numpy as npy

markList = [
    91,97,98,100,98,100
]

markTuple = (
    92,93,96,99,90,100
)

arrayList = npy.array(markList)
arrayTuple = npy.array(markTuple)

slicedArray = npy.split(arrayList,3)
slicedArray1 = npy.split(arrayTuple,3)
print(
    f"List Array:{arrayList}\n"
    f"Tuple Array:{arrayTuple}\n"
    f"Sliced List Array:{slicedArray}\n"
    f"Sliced Tuple Array:{slicedArray1}"
)

