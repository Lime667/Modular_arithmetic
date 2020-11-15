
template = """

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

MODE : 
[1] Find somes congruences between 2 numbers on a given interval. 
[2] Check if two numbers are congruent modulo n. (for a,b,n given)
[3] Check if a number is invertible in a given ring.
[] Developpement

Selected mode : """



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

def congru(a,b):
    pol = input("Enter two numbers to set the interval (empty is 2-100) : ")

    if pol == "":
        print("default selected : interval between 2-100")
        c = []
        for x in range(2,100):
            if a%x == b%x:
                c.append(str(a)+" ≡ "+str(b)+" modulo "+str(x))
                print(a,"≡",b,"modulo",x)
        exp_res(c)
    else:
        pal = pol.split("-")
        print(pal)
        min,max = int(pal[0]),int(pal[1])
        c = []
        for x in range(min,max):
            if a%x == b%x:
                c.append(str(a)+" ≡ "+str(b)+" modulo "+str(x))
                print(a,"≡",b,"modulo",x)
        exp_res(c)

def is_congru(a,b,n):
    if (a-b)%n == 0:
        print("[*] Congruence found.")
        print(a,"≡",b,"["+n+"]")
    else:
        print("[*]",a,"is not congruent to",b,"modulo",n)

def pgcd(a,b):
    if a > b:
        if b==0:
            return a
        else:
            r=a%b
            return(pgcd(b,r))
    if b > a:
        if a ==0:
            return b
        else:
            r=b%a
            return(pgcd(a,r))

def inverse(a,n):
    if pgcd(a,n) ==1:
        print(a,"is invertible in Z/"+str(n)+"Z")
        print("To doing that, we just calc the pgcd of",a,"and",n,". If they're relatively prime,",a,"is invertible.")
        print("Proof by the bachet-bezout theorem.")
    else:
        print(a,"is not invertible in Z/"+str(n)+"Z")


def main_menu():
    UIN = ""
    while UIN != "1" and UIN != "2" and UIN != "3":
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

main_menu()
