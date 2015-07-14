def alias(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)

alias(3, 23, 3, 3,a='hello',b=3,c='C')
