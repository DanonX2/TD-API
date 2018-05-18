def authrefresh(state):
    if state == 1:
        import time
        import requests
        import ast
        OAuthID = 'c20020807@AMER.OAUTHAP'
        RedirectURI = 'http://localhost:8080'
        authrefresh.access_token = 'FP2mcgG2Nfoo28UumFLsS5tLzw21Ax9RbMWuNtrFtna3g89Qv0GTr8DNN6y709LQ6VU5EksmJ3wYLfvJDq/BDBD7WkTBvqLaQJrGIvLJGn7VZB5X08v7anOBZ/h0vUpmgV2doOErgMIM7vtEMtOLE39wuVD6ff25MajRvYwwXDHSsP5XKW5rZUgO4NcSRyK97bLc54xlbX8MZmxaUE//ko2NMIVZW2QOXAVqfifgi0NiTDMX5RmNp+5/D9bLViuGJ6LZZoF/pm+9PsFWLRcP5Pp7QuLkwaJw41FPsoAG41eCvMM3yniVPwXHXdW1tub/n3pks00ESRCviaAFmeQlAVn9RjAEYl3DYrrxZ6q8i1SVZI6UXbid+Hw+UlgmRsyNlEwWhQKTwWurAaQ90UcaUTXcYm8fbLFZCmnnKABdo5L2Blc5RuBR/T6t8Nl/b483UmYMSmTCGQclgHtdjmR2F61wUZ4vbWFMh2xDPPmMx0nvY7Cgv+EyfG/u1wbDDs+Ckv2X7100MQuG4LYrgoVi/JHHvlTvbwrllf/+lvciK6F5zQo1EeKw72KQDfxxKJdh9Wv+uZj3kLeRy27lDqbUccbHKNtkCNFDMNTExir2Co0VVPSNoI2dlozLbpLGKTUMOXFRxGZ6BuZOh+VdcR5KfYikWpSk9UYtYsq0zpBguYcc1VO/yI5t+zXgVk8moKIjdRM8SuqSgCNo3ogOnV/WJwEMeezA689uaa/rEja+UyNFzu6V1JeBi2p7r8UtPa9zK3K0yws1OtteHtntcxnsY57F2HQiWehWGCTukma8xFW2wR/KEqtzUxY4h6rdXVfa4O+T78L94wCzo32KqqSmNdEYdlOTlcTmHRh7UGjwisABi5g2eNBa+kOAIRyEY3DIk8vc+ZuXez6VHR8vVixPYSe7c7hjRQ9PtKVw50al4du8Zpg8u4WAxuXs48qsjcCkJruMs1Kk548IpAm76+dcWrUnO+e80MxSrlrmO9mBfRT357bbiHsVmC3brRxfBpvDpQEsBnndS3PenmkoVCczU4ql/FgA2zRF212FD3x19z9sWBHDJACbC00B75E'
        authrefresh.refresh_token = 'ky40J5lYIV+pPihdDjQUXJfLsgbSnpNoXj+d+CeP3VqvTgoKFhmxdJz+kQN9Q7zXZ9gq825FRnWdJpdSHBXgJMjbRrZGBl8tuaM2GoelyBGXBeE1UQZvAG+kja9JiIRoTPph6j2sLUE2R9fMUGi+8dCILXQy2R37nQEFUiSJDxdlWxwuZRp13vq9Bz/Jjc6kZjswBFf/DMhcALW8zwQCqsAE8CKex+FEsxN1u7xE3tPc3oZttdyMfo614MmDXRO5OL6UZZl8j/uy2tTv793ugjsJnb7JuyqmZCDnKjTglS5r+dX3QZJbrNm1/paec69b/1vFhjMvDpWp9yiZeNvuTqIXKir/F0b1bhH1p1a+u+AldJRphtZemdIRNfUSWX3NLQ8mmrp5f6erp4ZDb7UGNW0zcaA69FplDkl8bwttGQHLVNe8Gll1Kqf/VD7100MQuG4LYrgoVi/JHHvlHsQrp1KjhgyB9m33vfzwWmKDqda7zfyPOT4eQdP2YhFgg8FYX+EQBlzJJTQBPEUJgOqQZiKVk+SqN6OQom9KE/CWzXjbA3/SMlsv2TUdT5xT9dyretcvHpJNDzv0t/PDkEuR4E8uSnSOIJykb8g7aORsx2Jl8PgKjVGLCd4GWKFoXYUHD5iiPFbh/yIZDnJBxQTnkaFWwsNtiiGVjH1u4aVzlvP1slPTNZavx9yleHCS7LrW//ZqaEwBRl5KjTUBE2h2lIF9X5iR9BbnlPBZ1gvf8x2NZ6S778Akj6s43II+Wqm8zp4uxOLhq3KQl14QH7kT9taksud7/HMhhIlP6DkzuDAErZqx92LA98ULo67WruhgU7+tXXFSv83cdWecxy9COY+qF+6OJ0TpVGt8OSo5M9rG9Ok5X/Lr98UgbMsn9B2Uq9gq3O76sh0=212FD3x19z9sWBHDJACbC00B75E'
        auth_url = 'https://api.tdameritrade.com/v1/oauth2/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = { 
            'grant_type': 'refresh_token',
            'refresh_token': authrefresh.refresh_token,
            'access_type': 'offline',
            'client_id': OAuthID ,
            'redirect_uri': RedirectURI
            }
        getauth = requests.post(auth_url, headers = headers, data=data)
        rawresponce = getauth.text
        authrefresh.decoded = ast.literal_eval(rawresponce)
        authrefresh.access_token = authrefresh.decoded['access_token']
        authrefresh.refresh_token = authrefresh.decoded['refresh_token']
    else:pass
