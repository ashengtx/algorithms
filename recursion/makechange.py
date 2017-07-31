"""
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
      # 这个newCoin是最优解中要用的最大的coin。因为如果最大的coin比这个小，那么minCoins[cents-j] + 1 将大于coinCount。而如果
   return minCoins[change]"""

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    """
    动态规划找零钱，从1开始
    """
    for cur_change in range(change+1):
        # 最大的找零个数是都用单位为1的，也就是本身
        min_count = cur_change
        # new_coin初始化为1。
        new_coin = 1
        # 尝试每种可用的coin，条件是比cur_change小
        for coin in [c for c in coinValueList if c <= cur_change]:
            if minCoins[cur_change - coin] + 1 < min_count:
                min_count = minCoins[cur_change - coin] + 1
                new_coin = coin
        minCoins[cur_change] = min_count
        coinsUsed[cur_change] = new_coin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 33
    clist = [1,5,8,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()
