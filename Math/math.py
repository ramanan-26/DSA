def countDigit(n):
    count = 0
    while n > 0:
        n % 10        # extracts the last digit
        count += 1
        n //= 10      # removes the last digit
    return count

print(countDigit(7877))
