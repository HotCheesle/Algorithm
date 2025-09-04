class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

# ccproduct[[{}, {}, {}, {}, {}], ] -> product[company][category]{ID: price}
# idproduct{ID: [company, category]}

ccproduct = []
idproduct = {}

def init() -> None:
    global ccproduct, idproduct
    ccproduct.clear()
    ccproduct = [
        [{}, {}, {}, {}, {}, {}] for _ in range(6)
    ]
    idproduct.clear()

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    global ccproduct, idproduct
    ccproduct[mCompany][mCategory][mID] = mPrice
    idproduct[mID] = [mCompany, mCategory]
    return len(ccproduct[mCompany][mCategory])

def closeSale(mID : int) -> int:
    global ccproduct, idproduct
    com_cat = idproduct.get(mID)
    if com_cat is None: 
        return -1
    else: 
        price = ccproduct[com_cat[0]][com_cat[1]].get(mID)
        idproduct.remove(mID)
        ccproduct[com_cat[0]][com_cat[1]].remove(mID)
        return price

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    global ccproduct, idproduct
    for key, value in ccproduct[mCompany][mCategory]: 
        ccproduct[mCompany][mCategory][key] -= value
        if ccproduct[mCompany][mCategory][key] <= 0: 
            closeSale(key)
    return len(ccproduct[mCompany][mCategory])

def show(mHow : int, mCode : int) -> RESULT:
    global ccproduct, idproduct
    min_heap = [0 for _ in range(50000)]
    return RESULT(-1, [0, 0, 0, 0, 0])