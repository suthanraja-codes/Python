

name ='suthan'
work = 'developer'
experiance = 'enga velai tharanga'

text = name + ' work is '+ work + ' experance vera kekkurange '+experiance
print(text)

text1 = '{} and {} and {}'
print(text1.format(name,work,experiance))

print('{} and {} and {}'.format(name,work,experiance))

print('{0} and {2} and {1} '.format('king','blue','pink'))

text3 = '{name} and {work} and {experiance}'
print(text3.format(name = 'nagu',work='nai meithal',experiance='1 hour'))

print('******{msg}*****'.format(msg='welcome'))