
# play out one thousand games of war.
results = [War().play() for _ in range(1000)]

print("After one thousand games of war, the shortest game had {} battles, the longest had {} battles, and the average was {}".format(
    min(results),
    max(results),
    sum(results) / len(results)
))
