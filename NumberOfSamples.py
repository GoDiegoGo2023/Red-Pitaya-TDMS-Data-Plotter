MAX=20000000
print('Input Parameters')
print('maximum number of samples is 20,000,000')
while True:
    try:
        f=float(input('Enter sampling frequency (Hz): '))
        t=float(input('Enter duration (s): '))
        samples=f*t
        if samples<=MAX:
            break
        print('sample size is too large, lower the frequency or duration')
    except ValueError:
        print()
        print('INVALID INPUT')
        print('please enter a number')
        print()
print()
print('=========================================')
print('Number of samples:', samples)
print('=========================================')