# s = 'foo'
# t = 'bar'
# print('barf' in 2 * (s + t))
# print(ord('foo'))
# s[::-3]
# s[-1::-3]
# s[:0:-3]
# s[-1:0:-3]

s="foobar"
s=s[::5]

print(s)
s=s[0] + s[-1]

print(s)
s=s[::-1][-1] + s[len(s)-1]

print(s)
s=s[::-5]

print(s)
s=s[::-1][::-5]
print(s)
s ="A multiplatform open source Binary Analysis and Reverse engineering Framework."
s=s[::-1][::-1] == s
print(s)
s ="A multiplatform open source Binary Analysis and Reverse engineering Framework."
s=s[:] == s
print(s)
s ="A multiplatform open source Binary Analysis and Reverse engineering Framework."
s=s[::-1][::-1] is s
print(s)
s ="A multiplatform open source Binary Analysis and Reverse engineering Framework."
s=s[:] is s
print(s)