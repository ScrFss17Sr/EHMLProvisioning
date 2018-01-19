import jwt


#from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives.asymmetric import dsa, rsa
#from cryptography.hazmat.primitives.serialization import load_pem_private_key
#from cryptography.hazmat.primitives.serialization import load_pem_public_key
#from Crypto.Util import asn1

from Crypto.PublicKey import RSA
from base64 import b64decode

_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAwThn6OO9kj0bchkOGkqYBnV1dQ3zU/xtj7Kj7nDd8nyRMcEWCtVzrzjzhiisRhlrzlRIEY82wRAZNGKMnw7cvCwNixcfcDJnjzgr2pJ+5/yDZUc0IXXyIWPZD+XdL+0EogC3d4+fqyvg/BF/F0t2hKHWr/UTXE6zrGhBKaL0d8rKfYd6olGWigFd+3+24CKI14zWVxUBtC+P9Fhngc9DRzkXqhxOK/EKn0HzSgotf5duq6Tmk9DCNM4sLW4+ERc6xzrgbeEexakabvax/Az9WZ4qhwgw+fwIhKIC7WLwCEJaRsW4m7NKkv+eJR2LKYesuQ9SVAJ3EXV86RwdnH4uAv7lQHsKURPVAQBlranSqyQu0EXs2N9OlWTxe+FyNkIvyZvoLrZl/CdlYc8AKxRm5rn2/88nkrYQ0XZSrnICM5FRWgVF2hn5KfZGwtBN85/D4Yck6B3ocMfyX7e4URUm9lRPQFUJGTXaZnEIge0R159HUwhTN1HvyXrs6uT1ZZmW+c3p47dw1+LmUf/hIf8zd+uvHQjIeHEJqxjqfyA8yqAFKRHKVFrwnwdMHIsRap2EKBhHMfeVf0P2th5C9MggYoGCvdIaIUgMBX3TtCdvGrcWML7hnyS2zkrlA8SoKJnRcRF2KxWKs355FhpHpzqyZflO5l98+O8wOsFjGpL9d0ECAwEAAQ=='
_audience = 'sb-eh-xsuaa-demo!t1855'



def getPublicKey():
    keyDER = b64decode(_key)
    keyPub = RSA.importKey(keyDER)

    return keyPub.publickey().exportKey()

def validateJWTToken(encoded):

    keyPub = getPublicKey()
    e = encoded

    print(keyPub)
    print('encoded: \n' + e)

    if 'Bearer ' in encoded:
        e = e.strip('Bearer')
        e = e.strip(' ')
        print(e)

    try:
        jwt.decode(e, keyPub, algorithms='RS256', audience=_audience)
        return True
    except jwt.exceptions.DecodeError as e:
        print('-----------------------Error 1----------------------')
        return False
    except jwt.exceptions.InvalidAudience as e:
        print('-----------------------Error 2----------------------')
        return False
    except jwt.exceptions.ExpiredSignature as e:
        print('-----------------------Error 3----------------------')
        return False
    except jwt.exceptions.InvalidTokenError as e:
        print('-----------------------Error 4----------------------')
        print(e)
        return False
    except jwt.exceptions.InvalidAudienceError as e:
        print('-----------------------Error 5----------------------')
        return False
    except jwt.exceptions.ImmatureSignatureError as e:
        print('-----------------------Error 6----------------------')
        return False
    except jwt.exceptions.ImmatureSignatureError as e:
        print('-----------------------Error 7----------------------')
        return False
    except jwt.exceptions.InvalidKeyError as e:
        print('-----------------------Error 8----------------------')
        return False




if __name__ == '__main__':

   e = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhYWVlMjY5NTEyNTI0MmYxODM5ODg4NzU1Y2JiMDJlOCIsImV4dF9hdHRyIjp7ImVuaGFuY2VyIjoiWFNVQUEifSwic3ViIjoiODc2ZmFmYjgtZDBiNy00NzM4LTg2MGItMDVmZjE3MGI4ZTY2Iiwic2NvcGUiOlsib3BlbmlkIl0sImNsaWVudF9pZCI6InNiLWVoLXhzdWFhLWRlbW8hdDE4NTUiLCJjaWQiOiJzYi1laC14c3VhYS1kZW1vIXQxODU1IiwiYXpwIjoic2ItZWgteHN1YWEtZGVtbyF0MTg1NSIsImdyYW50X3R5cGUiOiJhdXRob3JpemF0aW9uX2NvZGUiLCJ1c2VyX2lkIjoiODc2ZmFmYjgtZDBiNy00NzM4LTg2MGItMDVmZjE3MGI4ZTY2Iiwib3JpZ2luIjoibGRhcCIsInVzZXJfbmFtZSI6InN2ZW4ucm9zZW56d2VpZ0Bzb3ZhbnRhLmNvbSIsImVtYWlsIjoic3Zlbi5yb3Nlbnp3ZWlnQHNvdmFudGEuY29tIiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIiwiYXV0aF90aW1lIjoxNTE2MzYxNDcwLCJyZXZfc2lnIjoiNjRlNTQxMDUiLCJpYXQiOjE1MTYzNjE0NzAsImV4cCI6MTUxNjQwNDY3MCwiaXNzIjoiaHR0cDovL2VodGVzdC5sb2NhbGhvc3Q6ODA4MC91YWEvb2F1dGgvdG9rZW4iLCJ6aWQiOiIwYWMwNjdlMi1kNjQ2LTRmZjQtYmI2Mi0wNzJiMzA2ZWExMmUiLCJhdWQiOlsic2ItZWgteHN1YWEtZGVtbyF0MTg1NSIsIm9wZW5pZCJdfQ.WvCAHqX8mp3wreKTydKPtntaagHUsdkd33oU55mNSk9Hd9q6pALdq1pSa1V1720b3ELChTksm58SGVojANCdtMrZEmnIcuYui_UNCGTce0FyHMiU90dS3HZSXcLA1FhYqx_qBK6uxFUWUaxv7UTPDyaPXl2KSHn4hy3A8NQOOV3Sl-d9IU7Qf8-aIDNcffUZN1TwOf7-etiyDe5ih15eGkYCKXmfx_LyS_zNOp2UIYkDkqNK9mBN29RGlVBT_4MVFaDEyFWrEaeMtdKKyHF_zgU10yLrpKaOfDlHW8PJ5A15ChlfwYCZ0qqQe9auL2dgVuuptwPkGH7kHoFbhOVlhf-teJsDa6fV1mueHIwMpBqD8SJ27bWtBiHNNPuLQ7eZ-4VvOE4cbA2CfmqAQsLU2O_uTiEYl6ZWRH90K_7Ttnzgx2tA8qXEp4eHiCi0dWJNPOKvYl1jPRLosmimGqVdcZrMLLAJKeF_2eiOKVDjoz07RgBAQT_fx8Kcqfdec1GODHaJnmqkps0s-DaPBrpGddR-k_BVGhUV4811-3iMBsKiFMKAHNBLqpOuKoNcwABJ2a0ovn2Mzly6cd3wFQrnD-RdXE3AwR_fFvp-xoBFGwgJ5cd9FWpFMN1ZcdQ3L4GjIWRepJQjUdcnOOhbtfCWDb6evimDeyU0qsZU9ZyJ0ls'
   res = validateJWTToken(e)
   print(res)
    #print(validateJWTToken(_encoded, keyPub.publickey().exportKey()))
