import datetime

test_list = [n for n in range(5)]
print(test_list)
for n in test_list:
    if n < 3:
        test_list.remove(n)

print(test_list)