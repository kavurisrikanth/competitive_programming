def BaseConverter(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d


tiny_url_length = 7
tiny_url_dict={}
full_url_dict={}
count=0
base62=BaseConverter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def make_tiny_url(fullURL):
    if (fullURL in full_url_dict):
        print("TinyURL already Exists"+full_url_dict[fullURL])
        return
    global count
    s=""
    k = count
    count += 1
    if k == 0:
        s="0000000"
        if s not in tiny_url_dict:
            tiny_url_dict[s]=fullURL
            full_url_dict[fullURL]=s
            print("tiny url for "+fullURL+" is https://ca.ke/"+s)
            return
        
    while k != 0:
        s=base62[k%62]+s
        k=k//62
    l=len(s)
    if l<tiny_url_length:
        for i in range(tiny_url_length-l):
            s="0"+s
    if s not in tiny_url_dict:
        tiny_url_dict[s]=fullURL
        full_url_dict[fullURL] = s
    print("tiny url for "+fullURL+" is https://ca.ke/"+s)


def take_user_input():
    while True:
        print("Enter \n\t1. Generate TinyURL\n\t2. Redirect TinyURL\nCtrl + C to stop.")
        
        user_input = int(input())
        
        if user_input == 1:
            full_url = input("Enter an URL to tiny-ify it : ")
            make_tiny_url(full_url)
            print('\n\n')
        elif user_input == 2:
            tiny_url = input("Enter a tiny url: ")
            if tiny_url_dict.get(tiny_url,None) is not None:
                print("redirecting to " + tiny_url_dict[tiny_url])
            else:
                print(tiny_url + " doesn't exist.\n\n")
        else:
            print("Invalid Input\n\n")
            
            
if __name__ == '__main__':
    take_user_input()