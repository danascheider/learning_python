foo = 127
foo = foo or 32

bar = ''
bar = bar or 'Conditional Bar'

baz = 80
baz = baz + 1 if bool(float(baz)) else None

print foo
print bar
print baz