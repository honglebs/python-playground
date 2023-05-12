# Birthday Candles

# [4, 4, 1, 2] --> 2
# find the tallest candle and count the occurence of them 

# ====== NOTES ======= #
candles = [4, 4, 1, 3, 1, 1, 5]


def birthdayCakeCandles(candles):

    # use max to find the tallest candle, init a count and set to 0
    tallest_candle = max(candles)
    count = 0

    # iterate through for each candle in candles 
    for candle in candles:
        # condition if it equals the tallest candle (aka, our max), then count +1
        if candle == tallest_candle:
            count += 1

    return count

print(birthdayCakeCandles(candles))
print(birthdayCakeCandles([2, 2, 3, 4, 4]))




