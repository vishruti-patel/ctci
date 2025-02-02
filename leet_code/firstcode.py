def main():
    nums = [i for i in range(1, 10)]
    l = len(nums)
    for i in range(1, l):
        ans = nums[i-1] + nums[i]
        print(f"sum of nums at idx:{i-1} and idx:{i} = {ans}")
        # nums[i] = ans


if __name__ == "__main__":
    main()