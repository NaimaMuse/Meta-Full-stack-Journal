http_status = 600

if http_status == 200 or http_status ==201:
    print('success')
elif http_status == 400:
    print('Bad reqesut')
elif http_status == 401:
    print('Not found')
elif http_status == 500 or http_status == 501:
    print('server not found')
else:
    print('unknown')

     
match http_status:
    case 200 | 2001:
        print('success')
    case 500 | 501:
        print('server not found')
    case 400 | 401:
        print('server not found')

 
    case _:
        print('unknown')




