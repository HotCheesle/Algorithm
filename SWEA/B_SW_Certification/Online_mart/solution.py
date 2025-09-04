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
        idproduct.pop(mID)
        ccproduct[com_cat[0]][com_cat[1]].pop(mID)
        return price

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    global ccproduct, idproduct
    rm_key = []
    for key in ccproduct[mCompany][mCategory]: 
        ccproduct[mCompany][mCategory][key] -= mAmount
        if ccproduct[mCompany][mCategory][key] <= 0: 
            rm_key.append(key)
    for rm in rm_key: 
        closeSale(rm)
    return len(ccproduct[mCompany][mCategory])

def show(mHow : int, mCode : int) -> RESULT:
    global ccproduct, idproduct
    product_list = [None for _ in range(50010)]
    idx = 0
    if mHow == 1: 
        for comp in range(1, 6): 
            for key, value in ccproduct[comp][mCode].items(): 
                product_list[idx] = (value, key)
                idx += 1
        min_list = sorted(product_list[:idx])
    if mHow == 2: 
        for list in ccproduct[mCode]: 
            for key, value in list.items(): 
                product_list[idx] = (value, key)
                idx += 1
        min_list = sorted(product_list[:idx])
    else: 
        for comp in range(1, 6): 
            for cate in range(1, 6): 
                for key, value in ccproduct[comp][cate].items(): 
                    product_list[idx] = (value, key)
                    idx += 1
        min_list = sorted(product_list[:idx])
    
    result_list = [0, 0, 0, 0, 0]
    if idx > 5: idx = 5
    elif idx == 0: idx = -1
    for i in range(idx): 
        result_list[i] = min_list[i][1]
    return RESULT(idx, result_list)