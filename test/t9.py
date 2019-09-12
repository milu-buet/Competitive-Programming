
import collections

def rearrangeBarcodes(barcodes):
    cnt = collections.Counter(barcodes).most_common()[::-1]
    #print(cnt)

    ref = [val for val, t in cnt for _ in range(t)]
    print(ref.pop)

    for i in range(0, len(barcodes), 2):
        barcodes[i] = ref.pop()
    for i in range(1, len(barcodes), 2):
        barcodes[i] = ref.pop()
    return barcodes


barcodes = [1,1,1,1,3,2,3,1]
ans = rearrangeBarcodes(barcodes)
print(ans)
