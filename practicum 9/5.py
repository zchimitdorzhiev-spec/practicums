with open('input.txt', 'r', encoding='utf-8') as sf, \
        open('output.txt', 'w', encoding='utf-8') as bh:
    nums = []

    for line in sf:
        line = line.strip()

        if line.isdigit():
            nums.append(int(line))

    if len(nums) > 2:
        bh.write(str(nums[0] / nums[1] + nums[2]))