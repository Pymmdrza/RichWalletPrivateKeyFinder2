from libcrypto import Wallet
from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool
import random
import string

# =========================================================================================
mmdrza = '''
             ||=======================================================================||
             ||- ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗ -||-                                   -||
             ||- ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║ -||-                                   -||
             ||- ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩ -||-    @@@@@@@@ @@@@@@@ @@@  @@@      -||
             ||--------------------------------||-    @@!        @@!   @@!  @@@      -||
             ||-| WebSite : Mmdrza.Com        -||-    @!!!:!     @!!   @!@!@!@!      -||
             ||-| Mail : Pymmdrza@gmail.com   -||-    !!:        !!:   !!:  !!!      -||
             ||-|                             -||-    : :: :::    :     :   : :      -||
             ||-| Github.Com/PyMmdrza         -||-  PrivateKey Rich Wallet Cracker   -||
             ||-|                             -||-                                   -||
             ||-----------------------------------------------------------------------||
             ||-|  Donate BTC Address Wallet  => 1MMDRZAcM6dzmdMUSV8pDdAPDFpwzve9Fc  -||
             ||=======================================================================||
-----------------------------------------------------------------------------------------------------------------
'''
# ============================================================================================

def getRandomHexString(length: int = 64) -> str:
    letters_and_digits = string.hexdigits.lower()
    return ''.join(random.choice(letters_and_digits) for i in range(length))
r = 1
cores = 8


def seek(r):
    filename = "eth500.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    print('\n\n\n\n\n\n\n\n\n\n\n\n', Fore.RED, str(mmdrza), Style.RESET_ALL, '\n')
    z = 1
    w = 0
    while True:
        hex64 = getRandomHexString(64)
        priv = str(hex64)
        hdwallet = Wallet(priv)
        addr = hdwallet.get_address(coin="ethereum")
        print(Fore.YELLOW, 'Total Scan:', Fore.WHITE, str(z), Fore.YELLOW, 'Winner Wallet:', Fore.GREEN, str(w),
              Fore.YELLOW, 'Checking Now ----- ETH Address', Fore.WHITE, str(addr), end='\r', flush=True)
        z += 1

        if addr in add:
            print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW,
                  'Total Scan Checking ----- ETH Address =', Fore.GREEN, str(addr), end='\r')
            w += 1
            z += 1
            f = open("EthereumRichWinnerWallet.txt", "a")
            f.write('\nAddress = ' + str(addr))
            f.write('\nPrivate Key = ' + str(priv))
            f.write('\n=========================================================\n')
            f.close()
            print('Winner information Saved On text file = ADDRESS ', str(addr))
            continue


seek(r)

if __name__ == '__main__':
    jobs = []
    for r in range(cores):
        p = multiprocessing.Process(target=seek, args=(r,))
        jobs.append(p)
        p.start()
