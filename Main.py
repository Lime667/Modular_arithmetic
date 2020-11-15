import os
banner = '''
███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗      █████╗ ██████╗ 
████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔══██╗██╔══██╗
██╔████╔██║██║   ██║██║  ██║██║   ██║██║     ███████║██████╔╝
██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══██║██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗██║  ██║██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
            █████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗███████╗████████╗██╗ ██████╗
            ██╔══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║██╔════╝╚══██╔══╝██║██╔════╝
            ███████║██████╔╝██║   ██║   ███████║██╔████╔██║█████╗     ██║   ██║██║     
            ██╔══██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██║██║     
            ██║  ██║██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗   ██║   ██║╚██████╗
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝

                        
This little script help you to find some congruences and more generally to work with a ring. 
This can be helpful when you're working with very large integer.
Was made in order to learn some basics mathematicals principes and help me
to do some calc in a ring.
'''
template = """
MODE :                                                              
[1] Find somes congruences between 2 numbers on a given interval.              |  [b] Print the banner
[2] Check if two numbers are congruent modulo n. (for a,b,n given)             |  [e] Exit
[3] Check if a number is invertible in a given ring.                           |
[] Developpement

Selected mode : """

class utils:
    def exp_res(c):
        export = input("Export results in txt file ? y/n ")
        if export == "y" or export == "Y":
            name = input("Path to file(including name file, empty is current folder): ")
            if name == "":
                name = "CongruenceExport.txt"
            else:
                name = name
            file = open(name, "w",encoding="utf-8")
            var = ""
            for i in c:
                var += i+"\n"
            file.write(var)
            file.close()
        else:
            pass
    
    def backtomenu():
        m = "value"
        while m!="":
            m = input("Press enter to go back to the menu...")
        main_menu()

    def pgcd(a,b):
        if a > b:
            if b==0:
                return a
            else:
                r=a%b
                return(utils.pgcd(b,r))
        if b > a:
            if a ==0:
                return b
            else:
                r=b%a
                return(utils.pgcd(a,r))

    def bezout_coef(a, b):
        if b == 0:
            return (1, 0)
        else:
            (u, v) = utils.bezout_coef(b, a % b)
            return (v, u - (a // b) * v)

def congru(a,b):
    pol = input("Enter two numbers to set the interval (empty is 2-100) : ")

    if pol == "":
        print("default selected : interval between 2-100")
        c = []
        for x in range(2,100):
            if a%x == b%x:
                c.append(str(a)+" ≡ "+str(b)+" modulo "+str(x))
                print(a,"≡",b,"modulo",x)
        utils.exp_res(c)
    else:
        pal = pol.split("-")
        print(pal)
        min,max = int(pal[0]),int(pal[1])
        c = []
        for x in range(min,max):
            if a%x == b%x:
                c.append(str(a)+" ≡ "+str(b)+" modulo "+str(x))
                print(a,"≡",b,"modulo",x)
        utils.exp_res(c)
        utils.backtomenu()


def is_congru(a,b,n):
    if (a-b)%n == 0:
        print("[*] Congruence found.")
        print(a,"≡",b,"["+n+"]")
    else:
        print("[*]",a,"is not congruent to",b,"modulo",n)
    utils.backtomenu()


def inverse(a,n):
    if utils.pgcd(a,n) ==1:
        print(a,"is invertible in Z/"+str(n)+"Z")
        print("To doing that, we just calc the pgcd of",a,"and",n,". If they're relatively prime,",a,"is invertible.")
        print("We can prove it by the bachet-bezout theorem.")
        print("Let's find the invert. We need to calcul the bezout relation between",a,"and",n,"\n")
        b,c = utils.bezout_coef(a,n)
        print(b%n,"is the invert of",a)
        print("The invert of",-b,"is",-a%n)
    else:
        print(a,"is not invertible in Z/"+str(n)+"Z")
    utils.backtomenu()

def main_menu():
    UIN = ""
    while UIN != "1" and UIN != "2" and UIN != "3" and UIN != "b" and UIN != "e":
        UIN = input(template)
    if UIN == "1":
        a,b = int(input("a : ")),int(input("b : "))
        congru(a,b)
    elif UIN == "2":
        a,b,n = int(input("a : ")),int(input("b : ")), int(input("n : "))
        is_congru(a,b,n)
    elif UIN == "3":
        a,n = int(input("number to check : ")), int(input("Ring value : "))
        inverse(a,n)
    elif UIN == "b":
        print(banner)
        backtomenu()
    elif UIN == 'e' or UIN == "E":
        exit("Thanks.")

if __name__ == "__main__":
    os.system('cls' if os.name =='nt' else "clear")
    print(banner)
    main_menu()
