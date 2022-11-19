def list_sum(l):
    total = 0
    for term in l:
        total += term
    return total

if __name__ == "__main__":
    nums = list(map(int, input("Nums: ").split()))
    print("Sum: %d" %list_sum(nums))
